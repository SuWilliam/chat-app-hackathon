# Requirements
Install docker and `docker-compose`: https://docs.docker.com/compose/install/

# Run
1. Run `docker-compose build` from the root directory
2. Run `docker-compose up` from the root directory
2. Navigate to `localhost:3000` to view frontend
3. Register a new account by clicking `Signup` on the top right corner
4. Input an email and a secure complex password
5. This should log you in (can click `Logout` and log back in if you choose to do so)

# Considerations
I implemented polling the server for new messages every 1 second in order to keep the chat room up to date. This has some performance issues in the production environment since we don't want to keep making requests constantly. For time sakes and familiarity I implemented it this way. In the future I would use Django sockets to keep the chat up to date.
