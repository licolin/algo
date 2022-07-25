// copied from muduo/net/tests/TimerQueue_unittest.cc

#include "../base/EventLoop.h"
#include "../base/Logging.h"

#include <stdio.h>
#include <unistd.h>

int cnt = 0;
muduo::EventLoop* g_loop;

void printTid()
{
  printf("pid = %d, tid = %d\n", getpt(), muduo::CurrentThread::tid());
  printf("now %s\n", muduo::Timestamp::now().toString().c_str());
}

void print(const char* msg)
{
  printf("msg %s %s\n", muduo::Timestamp::now().toString().c_str(), msg);
  if (++cnt == 20)
  {
    g_loop->quit();
  }
}

int main()
{
    //muduo::Logger("./test_log", 500 * 1000 * 1000);
    //muduo::Logger::setLogLevel(muduo::Logger::LogLevel::TRACE);
    //muduo::Logger::setOutput("log_info.log");
  printTid();
  muduo::EventLoop loop;
  g_loop = &loop;

  print("main");
  /*loop.runEvery(1.5, std::bind(print, "once1"));
  loop.runEvery(1.8, std::bind(print, "once1.8"));
  loop.runEvery(0.5, std::bind(print, "once0.5"));
  loop.runEvery(1.0, std::bind(print, "once1.0"));
  loop.runAfter(3.5, std::bind(print, "once3.5"));
  loop.runEvery(2, std::bind(print, "every2"));
  loop.runEvery(3, std::bind(print, "every3"));*/

  loop.runAfter(1.5, std::bind(print, "once1.5"));
  loop.runAfter(0.5, std::bind(print, "once0.5"));
  loop.runAfter(1.0, std::bind(print, "once1.0"));
  

  loop.loop();
  print("main loop exits");
  sleep(2);
}
