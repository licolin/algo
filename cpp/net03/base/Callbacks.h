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

namespace muduo
{

// All client visible callbacks go here.

typedef std::function<void()> TimerCallback;

}

#endif  // MUDUO_NET_CALLBACKS_H
