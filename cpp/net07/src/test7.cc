#include "../base/Acceptor.h"
#include "../base/EventLoop.h"
#include "../base/InetAddress.h"
#include "../base/SocketsOps.h"
#include <stdio.h>
#include <unistd.h>

void newConnection(int sockfd, const muduo::InetAddress& peerAddr)
{
  printf("newConnection(): accepted a new connection from %s\n",
         peerAddr.toHostPort().c_str());
  ssize_t bytes_written = ::write(sockfd, "How are you?\n", 13);
  muduo::sockets::close(sockfd);
}

int main()
{
  printf("main(): pid = %d\n", getpt());

  muduo::InetAddress listenAddr(9981);
  muduo::EventLoop loop;

  muduo::Acceptor acceptor(&loop, listenAddr);
  acceptor.setNewConnectionCallback(newConnection);
  acceptor.listen();

  loop.loop();
}
