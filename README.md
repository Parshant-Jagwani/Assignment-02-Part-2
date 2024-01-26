# Assignment-02-Part-2
_Code base is available in Master branch_ 


#### 1.	Create a Docker file for the web application container which should include the necessary dependencies to run the web application. The web application should display a simple "Hello, World!" message when accessed from a web browser. 
#### Ans: In this part I made a simple application in which, I added _app.py_ file [app.py](https://github.com/Parshant-Jagwani/Assignment-02-Part-2/blob/master/app.py) and _requirements.txt_ file [requirements.txt](https://github.com/Parshant-Jagwani/Assignment-02-Part-2/blob/master/requirements.txt) at this stage app as up and running in vscode.

#### 2.	Create a Docker file for the database container which should include the necessary dependencies to run the database. You can use any database of your choice (e.g.,MySQL, PostgreSQL, MongoDB, etc.). 
#### Ans: In this part I added  _Dockerfile_ file [Dockerfile](https://github.com/Parshant-Jagwani/Assignment-02-Part-2/blob/master/Dockerfile) and made some changes in _app.py_ and _requirements.txt_ file ```psycopg2-binary==2.9.1 Werkzeug==2.0.1```

#### 3.	Create a docker-compose.yml file that defines the two services - web and database. The web service should be linked to the database service using Docker Compose networking. 
#### Ans: Created  _docker-compose_ file [docker-compose.yml](https://github.com/Parshant-Jagwani/Assignment-02-Part-2/blob/master/docker-compose.yml) and added in _app.py_ in ``` @app.route('/data')``` route and commected to web-app with database by linking ```depends_on: - database``` with the database.


#### 4.	Use the docker-compose up command to build and run the application. Verify that the web application is accessible from a web browser and that the database is running. 

#### TO initializing the docker-compose  with ```--no-cashe``` tag due to, I tried many times it was picking build from cache 
``` docker-compose build --no-cache ``` 
### Out-put
```
C:\Users\parsh\OneDrive\Desktop\Devops Training\Docker-Compose\Assignment-02-Part2>docker-compose build --no-cache
[+] Building 58.3s (13/13) FINISHED                                                            docker:default
 => [web internal] load build definition from Dockerfile                                                 0.1s
 => => transferring dockerfile: 646B                                                                     0.0s
 => [web internal] load .dockerignore                                                                    0.0s
 => => transferring context: 2B                                                                          0.0s
 => [web internal] load metadata for docker.io/library/python:3.9                                        4.0s
 => [web auth] library/python:pull token for registry-1.docker.io                                        0.0s
 => [web 1/7] FROM docker.io/library/python:3.9@sha256:3d9dbe78e1f45ed2eb525b462cdb02247cc0956713325aee  0.0s
 => [web internal] load build context                                                                    0.1s
 => => transferring context: 1.30kB                                                                      0.0s
 => CACHED [web 2/7] WORKDIR /app                                                                        0.0s
 => [web 3/7] RUN apt-get update && apt-get install -y python3-pip                                      28.7s
 => [web 4/7] RUN pip install --upgrade pip setuptools                                                  16.2s
 => [web 5/7] COPY requirements.txt .                                                                    0.2s
 => [web 6/7] RUN pip install --no-cache-dir -r requirements.txt                                         7.5s
 => [web 7/7] COPY . .                                                                                   0.2s
 => [web] exporting to image                                                                             1.2s
 => => exporting layers                                                                                  1.2s
 => => writing image sha256:f8b474938c6a1c7bfbcaa465d756f0335c8d39e1448560ee1707243b213d1831             0.0s
 => => naming to docker.io/library/assignment-02-part2-web
```
#### TO up the comtainer used bellow command, it was building successfully but unable to run on the browser.  

``` docker-compose up ``` 

#### Output

```
C:\Users\parsh\OneDrive\Desktop\Devops Training\Docker-Compose\Assignment-02-Part2>docker-compose up
[+] Running 2/2
 ✔ Container assignment-02-part2-database-1  Created                                                    22.8s
 ✔ Container assignment-02-part2-web-1       Created                                                     0.5s
Attaching to database-1, web-1
database-1  | The files belonging to this database system will be owned by user "postgres".
database-1  | This user must also own the server process.
database-1  |
database-1  | The database cluster will be initialized with locale "en_US.utf8".
database-1  | The default database encoding has accordingly been set to "UTF8".
database-1  | The default text search configuration will be set to "english".
database-1  |
database-1  | Data page checksums are disabled.
database-1  |
database-1  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
database-1  | creating subdirectories ... ok
database-1  | selecting dynamic shared memory implementation ... posix
database-1  | selecting default max_connections ... 100
database-1  | selecting default shared_buffers ... 128MB
database-1  | selecting default time zone ... Etc/UTC
database-1  | creating configuration files ... ok
database-1  | running bootstrap script ... ok
web-1       |  * Serving Flask app 'app' (lazy loading)
web-1       |  * Environment: production
web-1       |    WARNING: This is a development server. Do not use it in a production deployment.
web-1       |    Use a production WSGI server instead.
web-1       |  * Debug mode: on
web-1       |  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
web-1       |  * Restarting with stat
database-1  | performing post-bootstrap initialization ... ok
web-1       |  * Debugger is active!
web-1       |  * Debugger PIN: 137-111-636
database-1  | initdb: warning: enabling "trust" authentication for local connections
database-1  | You can change this by editing pg_hba.conf or using the option -A, or
database-1  | --auth-local and --auth-host, the next time you run initdb.
database-1  | syncing data to disk ... ok
database-1  |
database-1  |
database-1  | Success. You can now start the database server using:
database-1  |
database-1  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
database-1  |
database-1  | waiting for server to start....2024-01-26 18:06:07.812 UTC [48] LOG:  starting PostgreSQL 13.13 (Debian 13.13-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
database-1  | 2024-01-26 18:06:07.828 UTC [48] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
database-1  | 2024-01-26 18:06:07.892 UTC [49] LOG:  database system was shut down at 2024-01-26 18:06:05 UTC
database-1  | 2024-01-26 18:06:07.930 UTC [48] LOG:  database system is ready to accept connections
database-1  |  done
database-1  | server started
database-1  | CREATE DATABASE
database-1  |
database-1  |
database-1  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
database-1  |
database-1  | waiting for server to shut down....2024-01-26 18:06:18.426 UTC [48] LOG:  received fast shutdown request
database-1  | 2024-01-26 18:06:18.580 UTC [48] LOG:  aborting any active transactions
database-1  | 2024-01-26 18:06:18.602 UTC [48] LOG:  background worker "logical replication launcher" (PID 55) exited with exit code 1
database-1  | 2024-01-26 18:06:18.640 UTC [50] LOG:  shutting down
database-1  | ..2024-01-26 18:06:20.570 UTC [48] LOG:  database system is shut down
database-1  |  done
database-1  | server stopped
database-1  |
database-1  | PostgreSQL init process complete; ready for start up.
database-1  |
database-1  | 2024-01-26 18:06:21.758 UTC [1] LOG:  starting PostgreSQL 13.13 (Debian 13.13-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
database-1  | 2024-01-26 18:06:21.758 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
database-1  | 2024-01-26 18:06:21.758 UTC [1] LOG:  listening on IPv6 address "::", port 5432
database-1  | 2024-01-26 18:06:22.435 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
database-1  | 2024-01-26 18:06:23.041 UTC [63] LOG:  database system was shut down at 2024-01-26 18:06:20 UTC
database-1  | 2024-01-26 18:06:23.504 UTC [1] LOG:  database system is ready to accept connections
```
#### 5.	Modify the Docker file for the web application container to include a new feature (e.g., a new message, a new page, etc.). Rebuild the web application container and  redeploy the application using docker-compose. Verify that the new feature is working  as expected. 

#### Ans:  Modified the new-feature buy giving new route in app.py, but it was also unable to run on browser code is given bellow.
```
@app.route('/new-feature')
def new_feature():
    # Insert data into PostgreSQL
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO mytable (column1, column2) VALUES ('value1', 'value2');")
    connection.commit()
    connection.close()

    return 'This is the new feature! Data posted to PostgreSQL.'
```
#### for Removing the application and rebuit commands are given bellow
```
docker-compose rm
docker-compose build --no-cache
docker-compose up
```

#### 6.	Implement a backup strategy for the database. This can be achieved using a Docker volume or by running a backup script periodically. 

#### Ans:  For Backup, I created _Volume_ in Docker Desktop named as ```Assignment-data-backup```` and command is given bellow which created backup.

```
docker run -v Assignment-data-backup:/var/lib/postgresql/data b39e2ef5216b
```
#### ```-v``` represted the volume tag, ```Assignment-data-backup``` is _volume-Name_  , ```/var/lib/postgresql/data``` is directory from which database's backup will be maintained, and finally ```b39e2ef5216b``` Database's Container-ID


### Task 7,8, 9 Unable to Perform.

#### 7.	Implement a scaling strategy for the web application. This can be achieved by using the docker-compose scale command to create multiple instances of the web service. Verify that the web application is accessible and working correctly when scaled.


#### 8.	Implement a monitoring strategy for the application. This can be achieved by using a tool like Prometheus or Grafana to monitor the health and performance of the containers. 


#### 9.	Create a README.md file and document your findings for each command. For each command, provide a brief description of what it does, followed by the output and logs generated by the command. Ensure that the README.md file is well-organized, easy to read, and contains all necessary information.


#### 10.	Push the codebase for the sample application to your GitHub repository (create a new one for this part)

#### For initializing the Git, Adding the Git in project and maintaining the comment  used following commands  and made a project in GitHub Named as ```Assignment-02-Part-2```

#### CMDs
```
git init
git add .
git commit -m "Creating Assignment-02-Part-2 Git Repo"
```

#### Output
```
PS C:\Users\parsh\OneDrive\Desktop\Devops Training\Docker-Compose\Assignment-02-Part2> git init
Initialized empty Git repository in C:/Users/parsh/OneDrive/Desktop/Devops Training/Docker-Compose/Assignment-02-Part2/.git/
PS C:\Users\parsh\OneDrive\Desktop\Devops Training\Docker-Compose\Assignment-02-Part2> git add .
PS C:\Users\parsh\OneDrive\Desktop\Devops Training\Docker-Compose\Assignment-02-Part2> git add .
PS C:\Users\parsh\OneDrive\Desktop\Devops Training\Docker-Compose\Assignment-02-Part2>  git commit -m "Creating Assignment-02-Part-2 Git Repo"
[master (root-commit) 569b375] Creating Assignment-02-Part-2 Git Repo
 4 files changed, 85 insertions(+)
 create mode 100644 Dockerfile
 create mode 100644 app.py
 create mode 100644 docker-compose.yml
 create mode 100644 requirements.txt
```

####  For staging and pushing the code in [Assignment-02-Part-2](https://github.com/Parshant-Jagwani/Assignment-02-Part-2/tree/master)
```
git remote add origin https://github.com/Parshant-Jagwani/Assignment-02-Part-2
git push --set-upstream origin master
```

#### Output
```
PS C:\Users\parsh\OneDrive\Desktop\Devops Training\Docker-Compose\Assignment-02-Part2> git remote add origin https://github.com/Parshant-Jagwani/Assignment-02-Part-2
PS C:\Users\parsh\OneDrive\Desktop\Devops Training\Docker-Compose\Assignment-02-Part2> git push --set-upstream origin master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 8 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 1.37 KiB | 1.37 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
remote:
remote: Create a pull request for 'master' on GitHub by visiting:
remote:      https://github.com/Parshant-Jagwani/Assignment-02-Part-2/pull/new/master
remote:
To https://github.com/Parshant-Jagwani/Assignment-02-Part-2
 * [new branch]      master -> master
branch 'master' set up to track 'origin/master'.
```
