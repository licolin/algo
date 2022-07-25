// excerpts from http://code.google.com/p/muduo/
//
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.
//
// Author: Shuo Chen (chenshuo at chenshuo dot com)

#ifndef MUDUO_NET_CALLBACKS_H
#define MUDUO_NET_CALLBACKS_H

#include <functional>
#include <memory>

#include "Timestamp.h"
#include "Buffer.h"

namespace muduo
{

// All client visible callbacks go here.

    class TcpConnection;
    typedef std::shared_ptr<TcpConnection> TcpConnectionPtr;

    typedef std::function<void()> TimerCallback;
    typedef std::function<void(const TcpConnectionPtr&)> ConnectionCallback;
    typedef std::function<void(const TcpConnectionPtr&,
        Buffer* buf,
        Timestamp)> MessageCallback;
    typedef std::function<void(const TcpConnectionPtr&)> CloseCallback;
}

#endif  // MUDUO_NET_CALLBACKS_H
