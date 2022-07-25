// excerpts from http://code.google.com/p/muduo/
//
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.
//
// Author: Shuo Chen (chenshuo at chenshuo dot com)

#include "../base/TcpConnection.h"

#include "../base/Logging.h"
#include "../base/Channel.h"
#include "../base/EventLoop.h"
#include "../base/Socket.h"
#include "../base/SocketsOps.h"

// #include <boost/bind.hpp>

#include <errno.h>
#include <stdio.h>
#include <unistd.h>

using namespace muduo;
// loop 与 sockfd(tcp连接客户端文件描述符) 绑定到channel_
// 貌似到这里 有多个channel 公用一个loop
// 一个文件描述符只属于一个channel
TcpConnection::TcpConnection(EventLoop* loop,
                             const std::string& nameArg,
                             int sockfd,
                             const InetAddress& localAddr,
                             const InetAddress& peerAddr)
  : loop_(CHECK_NOTNULL(loop)),
    name_(nameArg),
    state_(kConnecting),
    socket_(new Socket(sockfd)),
    channel_(new Channel(loop, sockfd)),
    localAddr_(localAddr),
    peerAddr_(peerAddr)
{
  LOG_DEBUG << "TcpConnection::ctor[" <<  name_ << "] at " << this
            << " fd=" << sockfd;
  channel_->setReadCallback(
      std::bind(&TcpConnection::handleRead, this,std::placeholders::_1));
  channel_->setWriteCallback(
      std::bind(&TcpConnection::handleWrite, this));
  channel_->setCloseCallback(
      std::bind(&TcpConnection::handleClose, this));
  channel_->setErrorCallback(
      std::bind(&TcpConnection::handleError, this));
}

TcpConnection::~TcpConnection()
{
  LOG_DEBUG << "TcpConnection::dtor[" <<  name_ << "] at " << this
            << " fd=" << channel_->fd();
}

void TcpConnection::connectEstablished()
{
  loop_->assertInLoopThread();
  assert(state_ == kConnecting);
  setState(kConnected);
  channel_->enableReading();

  connectionCallback_(shared_from_this());
}

//void TcpConnection::connectDestroyed()
//{
//    loop_->assertInLoopThread();
//    assert(state_ == kConnected);
//    setState(kDisconnected);
//    channel_->disableAll();
//    connectionCallback_(shared_from_this());
//
//    loop_->removeChannel(get_pointer(channel_));
//}

void TcpConnection::connectDestroyed()
{
    loop_->assertInLoopThread();
    if (state_ == kConnected)
    {
        std::cout << "TcpConnection::connectDestroyed and current state is kConnected" << std::endl;
        setState(kDisconnected);
        channel_->disableAll();

        connectionCallback_(shared_from_this());
    }
    channel_->remove();
}

void TcpConnection::handleRead(Timestamp receiveTime)
{
    int savedErrno = 0;
    ssize_t n = inputBuffer_.readFd(channel_->fd(), &savedErrno);
    if (n > 0) {
        messageCallback_(shared_from_this(), &inputBuffer_, receiveTime);
    }
    else if (n == 0) {
        std::cout << "first handleRead then handleClose" << std::endl;
        handleClose();
    }
    else {
        errno = savedErrno;
        LOG_SYSERR << "TcpConnection::handleRead";
        handleError();
    }
}

void TcpConnection::handleWrite()
{
}

void TcpConnection::handleClose()
{
    std::cout << "handle close" << std::endl;
    loop_->assertInLoopThread();
    LOG_TRACE << "TcpConnection::handleClose state = " << state_;
    assert(state_ == kConnected);
    setState(kDisconnected);
    // we don't close fd, leave it to dtor, so we can find leaks easily.
    channel_->disableAll();
    //closeCallback_(shared_from_this());
    TcpConnectionPtr guardThis(shared_from_this());
    connectionCallback_(guardThis);
    // must be the last line
    closeCallback_(guardThis);
}

void TcpConnection::handleError()
{
    int err = sockets::getSocketError(channel_->fd());
    LOG_ERROR << "TcpConnection::handleError [" << name_
        << "] - SO_ERROR = " << err << " " << strerror_tl(err);
}
