# 📖 Introduction to `curl`

## 📝 Background

`curl` (Client URL) is a command-line tool for transferring data to or from a network server using various protocols like HTTP, HTTPS, FTP, etc. It is widely used for:
- **Testing and interacting with RESTful APIs** 📡
- **Diagnosing server issues** 🛠️
- **Quickly prototyping API requests** ⚡

---

## 🛠️ Basic Usage

### 🔹 Fetch a Web Page
```sh
curl http://example.com
```
📌 Displays the raw content of the requested page.

---

## 🔎 Fetch Data from an API

### 📌 Get Posts from JSONPlaceholder
```sh
curl https://jsonplaceholder.typicode.com/posts
```
📌 Returns a JSON array containing posts.

### 📌 Display Only the Response Headers
```sh
curl -I https://jsonplaceholder.typicode.com/posts
```
📌 Shows only the HTTP headers, useful for checking **status codes**, **content types**, **cache**, etc.

---

## ⚙️ Advanced Options Usage

### 🔹 Perform a POST Request
```sh
curl -X POST -d "title=foo&body=bar&userId=1" \
     https://jsonplaceholder.typicode.com/posts
```
📌 Simulates adding a post. The JSONPlaceholder API returns a response confirming the addition with an `id` = 101.

### 🔹 Send JSON Data with Specific Headers
```sh
curl -X POST -H "Content-Type: application/json" \
     -d '{"title": "foo", "body": "bar", "userId": 1}' \
     https://jsonplaceholder.typicode.com/posts
```
📌 Adds a `Content-Type: application/json` header to specify that the data is in JSON format.

### 🔹 Format JSON Output (Requires `jq`)
```sh
curl -s https://jsonplaceholder.typicode.com/posts | jq
```
📌 `jq` allows for more readable and filtered JSON output.

---

## 📌 Expected Results

✅ `curl --version` displays the installed version details.
✅ `curl https://jsonplaceholder.typicode.com/posts` returns posts in JSON format.
✅ `curl -I ...` displays only the HTTP headers.
✅ A `POST` request returns a response confirming data creation.

📌 **Tip**: Add `-v` to see request details, and `-o file.txt` to save output to a file.

