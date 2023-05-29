### Initial step
1. Generate a tarball containing the Dockerfile meant to execute the task and any additional scripts and files
    - Max size is 50MB
    - Filename solution.tar.gz
    - Dockerfile is casesentive filename
2. Upload this to the challenge using REST-API call
    - `curl https://play.livectf.com/api/challenges/[CHALLENGE_ID] -F exploit=@solution.tar.gz -H "X-LiveCTF-Token: ticket{PriceAgent9040n23:xCI4jlISX405VzK9U9X-pE3jOdcuXdf6LwKq36Y4kpuEYl51}"`
3. This will return the Exploit-ID which is required for checking any status on the submitted task, eg. error messages
    - Eg. `{"exploit_id": "5a58e1fa-28e0-4347-b48c-745a330db560", ...}`
```lang=bash
$ tar czf solution.tar.gz Dockerfile solve.py
$ curl https://play.livectf.com/api/challenges/7 -F exploit=@solution.tar.gz -H "X-LiveCTF-Token: ticket{PriceAgent9040n23:xCI4jlISX405VzK9U9X-pE3jOdcuXdf6LwKq36Y4kpuEYl51}"

{"exploit_id":"5a58e1fa-28e0-4347-b48c-745a330db560","team_id":88,"challenge_id":7,"archive_id":"e652ccdd-c0dd-4b75-9315-ab60e30ca59b","status":"Submitted","score_awarded":null,"submission_time":"2023-05-27T11:16:53.468737977","run_duration":null}  
```


### Getting end status
Before completion it wil not return a final status, but the "building" or "running" status.  Wait until finished running.

1. Query the REST-api using the exploit ID, and team token
    - Eg. `curl https://play.livectf.com/api/exploits/5a58e1fa-28e0-4347-b48c-745a330db560 -H "X-LiveCTF-Token: ticket{PriceAgent9040n23:xCI4jlISX405VzK9U9X-pE3jOdcuXdf6LwKq36Y4kpuEYl51}"`

```lang=bash
$ curl https://play.livectf.com/api/exploits/5a58e1fa-28e0-4347-b48c-745a330db560 -H "X-LiveCTF-Token: ticket{PriceAgent9040n23:xCI4jlISX405VzK9U9X-pE3jOdcuXdf6LwKq36Y4kpuEYl51}"

{"exploit_id":"5a58e1fa-28e0-4347-b48c-745a330db560","team_id":88,"challenge_id":7,"archive_id":"e652ccdd-c0dd-4b75-9315-ab60e30ca59b","status":"Running","score_awarded":null,"submission_time":"2023-05-27T11:16:53.468737","run_duration":null} 
```


### Example Dockerfile
```
FROM livectf/livectf:quals-exploit
COPY solve.py /
WORKDIR /
CMD ["python3", "solve.py"]
```

### Example python solution script
```lang=Python
from pwn import *
HOST = os.environ.get('HOST', 'localhost')
PORT = 31337
r = remote(HOST, int(PORT))
r.recvline_contains(b'Give me input: ')
r.sendline(b'WIN')
r.recvline_contains(b'You sent: ')
r.sendline(b'./submitter')
flag = r.recvline_contains(b'LiveCTF{').decode().strip()
log.info('Flag: %s', flag)
```