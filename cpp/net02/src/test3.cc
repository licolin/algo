#include "../base/Channel.h"
#include "../base/EventLoop.h"

#include <stdio.h>
#include <sys/timerfd.h>
#include <unistd.h>
#include <iostream>

muduo::EventLoop* g_loop;

void timeout()
{
  printf("Timeout!\n");
  g_loop->quit();
}

int main()
{
  muduo::EventLoop loop;
  g_loop = &loop;

  int timerfd = ::timerfd_create(CLOCK_MONOTONIC, TFD_NONBLOCK | TFD_CLOEXEC);
  muduo::Channel channel(&loop, timerfd);
  channel.setReadCallback(timeout);
  channel.enableReading();

  std::cout << "timer start!" << std::endl;
  struct itimerspec howlong;
  bzero(&howlong, sizeof howlong);
  howlong.it_value.tv_sec = 6;
  ::timerfd_settime(timerfd, 0, &howlong, NULL);
  std::cout << "timer end!" << std::endl << std::endl;
  loop.loop();
  std::cout << "loop end!" << std::endl;
  ::close(timerfd);
}
