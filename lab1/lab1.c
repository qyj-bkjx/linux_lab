#include <stdio.h>
#include <unistd.h>
#include <sys/select.h>
#define BUF_SIZE 1024
int main()
{
    //创建两个管道
    int pipe1[2], pipe2[2];
    if (pipe(pipe1) == -1 || pipe(pipe2) == -1)
    {
        perror("pipe error");
        return -1;
    }
   //获取管道的文件描述符
    int fd1 = pipe1[0]; //管道1的读端
    int fd2 = pipe2[1]; //管道2的写端
   //定义一个fd_set类型的变量readset，并初始化为全零
    fd_set readset;
    FD_ZERO(&readset);
   //将fd1加入到readset中
    FD_SET(fd1, &readset);
   //定义一个timeval类型的变量timeout，并设置超时时间为5秒
    struct timeval timeout;
    timeout.tv_sec = 5;
    timeout.tv_usec = 0;
    char buf[BUF_SIZE]; //缓冲区
    int result;         //select函数的返回值
    int len;            //读取或写入的字节数
    while (1)
    {
        //调用select函数，监视fd1是否有数据可读
        result = select(fd1 + 1, &readset, NULL, NULL, &timeout);            //有文件描述符发生了变化
            if (W(fd1, &readset))
            {
                //fd1有数据可读，从fd1中读取数据
                len = read(fd1, buf, BUF_SIZE); //读取成功，将数据写入到fd2中去
                write(fd2, buf, len);
                
            }
       //重置readset和timeout，因为select函数会修改它们的值
        FD_ZERO(&readset);
        FD_SET(fd1, &readset);
        timeout.tv_sec = 5;
        timeout.tv_usec = 0;
    }
    //关闭管道
    close(pipe1[0]);
    close(pipe1[1]);
    close(pipe2[0]);
    close(pipe2[1]);

    return 0;
}