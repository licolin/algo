// excerpts from http://code.google.com/p/muduo/
//
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.
//
// Author: Shuo Chen (chenshuo at chenshuo dot com)

#include "../base/EventLoopThread.h"

#include "../base/EventLoop.h"

//#include <boost/bind.hpp>
#include <iostream>

using namespace muduo;

EventLoopThread::EventLoopThread()
  : loop_(NULL),
    exiting_(false),
    thread_(std::bind(&EventLoopThread::threadFunc, this)),
    mutex_(),
    cond_(mutex_)
{
}

EventLoopThread::~EventLoopThread()
{
  exiting_ = true;
  loop_->quit();
  thread_.join();
}

EventLoop* EventLoopThread::startLoop()
{
  assert(!thread_.started());
  thread_.start();
  {
    MutexLockGuard lock(mutex_);
    while (loop_ == NULL)
    {
      std::cout << "loop_ is NULL" << std::endl;
      cond_.wait();
    }
  }
  std::cout << "loop_ is not NULL" << std::endl;
  return loop_;
}

void EventLoopThread::threadFunc()
{
  EventLoop loop;

  {
    MutexLockGuard lock(mutex_);
    loop_ = &loop;
    cond_.notify();
  }

  loop.loop();
  //assert(exiting_);
}

