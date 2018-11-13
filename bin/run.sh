#!/bin/bash
docker run -d --name=canvas -p 80:3000 -p 5432:5432 -e EMAIL_DELIVERY_METHOD=smtp -e SMTP_ADDRESS=smtp.gmail.com -e SMTP_PORT=587 -e SMTP_USER=test.canvas.lms.kz@gmail.com -e SMTP_PASS=huytran123 docker-canvas
