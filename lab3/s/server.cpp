#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/wait.h>
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

int main() {
    int listenfd, connfd;
    pid_t childpid;
    socklen_t clilen;
    struct sockaddr_in cliaddr, servaddr;

    listenfd = socket(AF_INET, SOCK_STREAM, 0);
    if (listenfd == -1) {
        perror("socket");
        exit(1);
    }

    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port = htons(PORT);

    if (bind(listenfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) == -1) {
        perror("bind");
        exit(1);
    }

    if (listen(listenfd, 10) == -1) {
        perror("listen");
        exit(1);
    }

    std::cout << "Server running on port " << PORT << std::endl;

    while (true) {
        clilen = sizeof(cliaddr);
        connfd = accept(listenfd, (struct sockaddr *)&cliaddr, &clilen);
        if (connfd == -1) {
            perror("accept");
            exit(1);
        }

        childpid = fork();
        if (childpid == -1) {
            perror("fork");
            exit(1);
        }

        if (childpid == 0) {
            close(listenfd);
            std::cout << "Client connected" << std::endl;

            while (true) {
                char buf[MAXLINE];
                int n = read(connfd, buf, MAXLINE);
                if (n == -1) {
                    perror("read");
                    exit(1);
                }
                if (n == 0) {
                    std::cout << "Client disconnected" << std::endl;
                    break;
                }

                buf[n] = '\0';
                handle_command(connfd, buf);
            }

            close(connfd);
            exit(0);
        }

        close(connfd);
        waitpid(-1, NULL, WNOHANG);
    }

    close(listenfd);
    return 0;
}

void handle_command(int sockfd, char* command) {
    char* token = strtok(command, " ");
    if (strcmp(token, "ls") == 0) {
        handle_ls(sockfd);
    } else if (strcmp(token, "get") == 0) {
        token = strtok(NULL, " ");
        handle_get(sockfd, token);
    } else if (strcmp(token, "put") == 0) {
        token = strtok(NULL, " ");
        handle_put(sockfd, token);
    } else if (strcmp(token, "exit") == 0) {
        handle_exit(sockfd);
    } else {
        std::cout << "Invalid command" << std::endl;
    }
}

void handle_ls(int sockfd) {
    char buf[MAXSIZE];
    FILE* fp = popen("ls", "r");
    if (fp == NULL) {
        perror("popen");
        exit(1);
    }

    while (fgets(buf, MAXSIZE, fp) != NULL) {
        std::cout<<"ls...\n";
        if (write(sockfd, buf, strlen(buf)) == -1) {
            perror("write");
            exit(1);
        }
    }
    buf[0]='@';
    buf[1]='\0';
    write(sockfd, buf, 2);
    if (pclose(fp) == -1) {
        perror("pclose");
        exit(1);
    }
    std::cout<<"close ls\n";
}

void handle_get(int sockfd, char* filename) {
    FILE* fp = fopen(filename, "rb");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }

    char buf[MAXSIZE];
    int n;
    while ((n = fread(buf, 1, MAXSIZE, fp)) > 0) {
        if (write(sockfd, buf, n) == -1) {
            perror("write");
            exit(1);
        }
    }

    fclose(fp);
    std::cout<<"finish get \n";
}

void handle_put(int sockfd, char* filename) {
    FILE* fp = fopen(filename, "wb");
    if (fp == NULL) {
        perror("fopen");
        exit(1);
    }

    char buf[MAXSIZE];
    int n;
    if ((n = read(sockfd, buf, MAXSIZE)) > 0) {
        if (fwrite(buf, 1, n, fp) != n) {
            perror("fwrite");
            exit(1);
        }
    }

    fclose(fp);
    std::cout<<"finish put\n";
}

void handle_exit(int sockfd) {
    std::cout<<"Client disconnected\n";
    close(sockfd);
    
    exit(0);
}