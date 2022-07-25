#include "../base/EventLoop.h"
#include "../base/EventLoopThread.h"
#include <stdio.h>
#include <unistd.h>
#include <iostream>

void runInThread()
{
  printf("runInThread(): pid = %d, tid = %d\n",
         getpid(), muduo::CurrentThread::tid());
}

int main()
{
  printf("main(): pid = %d, tid = %d\n",
         getpt(), muduo::CurrentThread::tid());

  muduo::EventLoopThread loopThread;
  muduo::EventLoop* loop = loopThread.startLoop();
  std::cout << "startloop end!" << std::endl;
  loop->runInLoop(runInThread);
  sleep(1);
  std::cout << "xxxxxxxxxxxxxxxxxxxxx" << std::endl;
  loop->runAfter(2, runInThread);
  sleep(3);
  loop->quit();

  printf("exit main().\n");
}
