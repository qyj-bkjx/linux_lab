#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <fcntl.h>
#include <errno.h>

#define PORT 8888
#define MAXLINE 1024
#define MAXSIZE 1024

void handle_command(int sockfd, char* command);
void handle_ls(int sockfd);
void handle_get(int sockfd, char* filename);
void handle_put(int sockfd, char* filename);
void handle_exit(int sockfd);
char filebuff[MAXSIZE];
int main() {
    int sockfd;
    struct sockaddr_in servaddr;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        perror("socket");
        exit(1);
    }

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");
    servaddr.sin_port = htons(PORT);

    if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) == -1) {
        perror("connect");
        exit(1);
    }

    std::cout << "Connected to server" << std::endl;

    while (true) {
        char buf[MAXLINE];
        std::cin.getline(buf, MAXLINE);
        handle_command(sockfd, buf);
    }

    close(sockfd);
    return 0;
}

void handle_command(int sockfd, char* command) {
    if (strcmp(command, "ls") == 0) {
        if (write(sockfd, command, strlen(command)) == -1) {
            perror("write");
            exit(1);
        }
        handle_ls(sockfd);
    } else if (strncmp(command, "get", 3) == 0) {
        std::cout<<"sys:get...\n";
        if (write(sockfd, command, strlen(command)) == -1) {
            perror("write");
            exit(1);
        }
        char* filename = command + 4;
        handle_get(sockfd, filename);
    } else if (strncmp(command, "put", 3) == 0) {
        std::cout<<"sys:put...\n";
        if (write(sockfd, command, strlen(command)) == -1) {
            perror("write");
            exit(1);
        }
        char* filename = command + 4;
        handle_put(sockfd, filename);
    } else if (strcmp(command, "exit") == 0) {
        std::cout<<"sys:exit\n";
        if (write(sockfd, command, strlen(command)) == -1) {
            perror("write");
            exit(1);
        }
        handle_exit(sockfd);
    } else {
        std::cout << "Invalid command" << std::endl;
    }
}

void handle_ls(int sockfd) {
    char buf[MAXSIZE];
    int n;
    while ((n = read(sockfd, buf, MAXSIZE)) > 0) {
        std::cout<<"ls..\n";
        buf[n] = '\0';
        if(buf[0]=='@') break;
        std::cout << buf;
   }
    std::cout<<"sys:finish ls\n";
}

void handle_get(int sockfd, char* filename) {
    FILE* fp = fopen(filename, "wb");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }

    char buf[MAXSIZE];
    int n;
    if ((n = read(sockfd, buf, MAXSIZE)) > 0) {
        std::cout<<"read and write..."<<std::endl;
        if (fwrite(buf, 1, n, fp) != n) {
            perror("fwrite");
            exit(1);
        }
    }
    std::cout<<"sys:finish get\n";
    fclose(fp);
}

void handle_put(int sockfd, char* filename) {
    FILE* fp = fopen(filename, "rb");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }

    char buf[MAXSIZE];
    int n;
    if ((n = fread(buf, 1, MAXSIZE, fp)) > 0) {
        if (write(sockfd, buf, n) == -1) {
            perror("write");
            exit(1);
        }
    }

    fclose(fp);
}

void handle_exit(int sockfd) {
    close(sockfd);
    exit(0);
}