// excerpts from http://code.google.com/p/muduo/
//
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.
//
// Author: Shuo Chen (chenshuo at chenshuo dot com)

#include "../base/Channel.h"
#include "../base/EventLoop.h"
#include "../base/Logging.h"

#include <sstream>

#include <poll.h>

using namespace muduo;

#include <sstream>

#include <poll.h>

using namespace muduo;

const int Channel::kNoneEvent = 0;
const int Channel::kReadEvent = POLLIN | POLLPRI;
const int Channel::kWriteEvent = POLLOUT;

// client 连接断开的情况  走的是readCallback_ 事件回调
Channel::Channel(EventLoop* loop, int fdArg)
    : loop_(loop),
    fd_(fdArg),
    events_(0),
    revents_(0),
    index_(-1),
    eventHandling_(false)
{
}

Channel::~Channel()
{
    assert(!eventHandling_);
}

void Channel::update()
{
    loop_->updateChannel(this);
}

void Channel::remove()
{
    assert(isNoneEvent());
    //addedToLoop_ = false;
    loop_->removeChannel(this);
}

void Channel::handleEvent(Timestamp receiveTime)
{
    std::cout << "Channel::handleEvent()" << std::endl;
    eventHandling_ = true;
    if (revents_ & POLLNVAL) {
        LOG_WARN << "Channel::handle_event() POLLNVAL";
    }

    if ((revents_ & POLLHUP) && !(revents_ & POLLIN)) {
        std::cout << "event closeCallback_()" << std::endl;
        LOG_WARN << "Channel::handle_event() POLLHUP";
        if (closeCallback_) closeCallback_();
    }
    if (revents_ & (POLLERR | POLLNVAL)) {
        std::cout << "event errorCallback_()" << std::endl;
        if (errorCallback_) errorCallback_();
    }
    if (revents_ & (POLLIN | POLLPRI | POLLRDHUP)) {
        std::cout << "event readCallback_()" << std::endl;
        if (readCallback_) readCallback_(receiveTime);
    }
    if (revents_ & POLLOUT) {
        std::cout << "event writeCallback_()" << std::endl;
        if (writeCallback_) writeCallback_();
    }
    eventHandling_ = false;
}