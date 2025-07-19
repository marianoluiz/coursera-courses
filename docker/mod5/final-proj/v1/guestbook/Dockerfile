# Please choose from the below set of Docker commands to complete your Dockerfile:

# COPY
# RUN
# ADD
# EXPOSE
# FROM
# CMD
# PUSH
# PULL
# WORKDIR

# PART 1: The Builder Stage
FROM golang:1.18 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy Go source code into the container
COPY main.go .

# Initialize a Go module (you can skip this if you already have go.mod locally)
RUN go mod init guestbook

# Download dependencies
RUN go mod tidy

# Build the Go application
RUN go build -o main main.go

# PART 2: The Final Image (for Running the App)
FROM ubuntu:18.04

# Set working directory in the final container
WORKDIR /app

# copies the compiled Go app (main) from the first stage and renames it guestbook. Now it's ready to run.
COPY --from=builder /app/main /app/guestbook

# Copy the compiled Go binary from the builder stage
COPY public/index.html /app/public/index.html
COPY public/script.js /app/public/script.js
COPY public/style.css /app/public/style.css
COPY public/jquery.min.js /app/public/jquery.min.js

# Expose port 3000 (your Go app should listen on this port)
EXPOSE 3000

# when the container starts, run your app called guestbook
CMD ["./guestbook"]