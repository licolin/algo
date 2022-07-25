// excerpts from http://code.google.com/p/muduo/
//
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.
//
// Author: Shuo Chen (chenshuo at chenshuo dot com)

#include "../base/Acceptor.h"

#include "../base/Logging.h"
#include "../base/EventLoop.h"
#include "../base/InetAddress.h"
#include "../base/SocketsOps.h"


using namespace muduo;
// acceptSocket_    通过createNonblockingOrDie创建 socket fd(服务端)
//  acceptChannel_ 通过该通道 监听 acceptSocket_.fd() 事件
Acceptor::Acceptor(EventLoop* loop, const InetAddress& listenAddr)
  : loop_(loop),
    acceptSocket_(sockets::createNonblockingOrDie()),
    acceptChannel_(loop, acceptSocket_.fd()),
    listenning_(false)
{
  acceptSocket_.setReuseAddr(true);
  acceptSocket_.bindAddress(listenAddr);
  // 给 acceptChannel_ 通道设置回调函数
  acceptChannel_.setReadCallback(
      std::bind(&Acceptor::handleRead, this));
}

void Acceptor::listen()
{
  loop_->assertInLoopThread();
  listenning_ = true;
  acceptSocket_.listen();
  acceptChannel_.enableReading();
}

void Acceptor::handleRead()
{
  loop_->assertInLoopThread();
  InetAddress peerAddr(0);
  //FIXME loop until no more
  int connfd = acceptSocket_.accept(&peerAddr);
  if (connfd >= 0) {
    if (newConnectionCallback_) {
      newConnectionCallback_(connfd, peerAddr);
    } else {
      sockets::close(connfd);
    }
  }
}

