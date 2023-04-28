#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define MAX_READERS 100
#define MAX_WRITERS 100
#define file 'test.txt'

pthread_rwlock_t rwlock;

int read_count = 0;

void *reader(void *arg) {
    int id = *(int *)arg;
    while (1) {
        // Acquire read lock
        pthread_rwlock_rdlock(&rwlock);
        read_count++;
        if (read_count == 1) {
            // Acquire write lock to prevent writers
            pthread_rwlock_wrlock(&rwlock);
        }
        printf("Reader %d is reading file\n", id);
        sleep(rand() % 2);
        read_count--;
        if (read_count == 0) {
            // Release write lock
            pthread_rwlock_unlock(&rwlock);
        }
        pthread_rwlock_unlock(&rwlock);
    }
}

void *writer(void *arg) {
    int id = *(int *)arg;
    while (1) {
        // Acquire write lock
        pthread_rwlock_wrlock(&rwlock);
        
        // Write to file
        printf("Writer %d is writing to file\n", id);
        sleep(rand() % 2);
        
        // Release write lock
        pthread_rwlock_unlock(&rwlock);
    }
}

int main() {
    // Initialize read-write lock
    pthread_rwlock_init(&rwlock, NULL);
    
    // Create reader threads
    pthread_t reader_threads[MAX_READERS];
    int reader_ids[MAX_READERS];
    for (int i = 0; i < MAX_READERS; i++) {
        reader_ids[i] = i;
        pthread_create(&reader_threads[i], NULL, reader, &reader_ids[i]);
    }
    
    // Create writer threads
    pthread_t writer_threads[MAX_WRITERS];
    int writer_ids[MAX_WRITERS];
    for (int i = 0; i < MAX_WRITERS; i++) {
        writer_ids[i] = i;
        pthread_create(&writer_threads[i], NULL, writer, &writer_ids[i]);
    }
    
    // Join threads
    for (int i = 0; i < MAX_READERS; i++) {
        pthread_join(reader_threads[i], NULL);
    }
    for (int i = 0; i < MAX_WRITERS; i++) {
        pthread_join(writer_threads[i], NULL);
    }
    
    // Destroy read-write lock
    pthread_rwlock_destroy(&rwlock);
    
    return 0;
}