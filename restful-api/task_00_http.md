# 🌐 Understanding HTTP and HTTPS

## 📌 Objectives
This guide explains the differences between **HTTP and HTTPS**, the structure of HTTP requests and responses, as well as the most common methods and status codes.

---

## 🔹 1. Differences Between HTTP and HTTPS

| Criterion      | HTTP                          | HTTPS                          |
|--------------|------------------------------|--------------------------------|
| **Security**  | Not secure (data in plaintext) | Secure with SSL/TLS encryption |
| **Port**      | 80                            | 443                            |
| **Certificate** | Not required                   | Uses an SSL certificate        |
| **Usage** | Basic sites, public content | Sites requiring security (payments, logins, etc.) |

**Why is HTTPS important?**
HTTPS protects data against theft and **Man-in-the-Middle (MITM)** attacks.

---

## 🔹 2. Structure of HTTP Requests and Responses

### 📍 **Example of an HTTP Request**
- **GET**: HTTP method used.
- **/index.html**: Requested resource.
- **HTTP/1.1**: Protocol version.
- **Host**: Server name.
- **User-Agent**: Browser information.

### 📍 **Example of an HTTP Response**
- **HTTP/1.1 200 OK**: Response status (success).
- **Server**: Type of server used.
- **Content-Type**: Type of content sent.

---

## 🔹 3. Common HTTP Methods and Status Codes

### 📍 **Common HTTP Methods**
| Method  | Description                          | Use Case             |
|----------|--------------------------------------|--------------------------------|
| **GET**   | Retrieves data               | Loading a web page          |
| **POST**  | Sends data to the server      | Submitting a form         |
| **PUT**   | Updates a resource           | Modifying a user profile |
| **DELETE**| Deletes a resource             | Removing a comment      |

### 📍 **Common HTTP Status Codes**
| Code  | Meaning          | Use Case                      |
|-------|------------------------|----------------------------------------|
| **200 OK** | Success              | Page loads normally         |
| **301 Moved Permanently** | Permanent redirection | A site changed its URL              |
| **403 Forbidden** | Access denied         | Page restricted to authorized users |
| **404 Not Found** | Resource not found | Requested page not available            |
| **500 Internal Server Error** | Server error       | Internal site issue         |

---

## 🎯 **Summary**
✅ **HTTPS** is more secure than **HTTP** due to SSL/TLS encryption.
✅ An HTTP request contains **methods, headers, and parameters**.
✅ **HTTP status codes** indicate the result of a request.

