# LiteStash

A key-value store for Python, built on SQLite with a NoSQL api and speed.

## Overview

The LiteStash Python project offers a lightning-fast, lightweight key-value storage for Python applications.  LiteStash provides a NoSQL API for seamless integration into your applications.  Optimal use for caching, session management, and other high-performance use cases.  LiteStash is for high-performance storage of key-value data that leverages SQLite's reliability and speed, optimized for scenarios where you need quick access to data.

## Key-Value Store
    
With a simple, NoSQL-like API, LiteStash is easy to integrate into your Python applications, especially web frameworks like FastAPI and Django.
Keys are hashed and indexed by Sqlite in the background.  Each database handles at most four tables across sixteen distinct database files.

## Features

* **Performance:** Stores data in memory for near-instantaneous access.
* **Pydantic Data Validation:** Ensures type safety and data integrity using Pydantic models.
* **Distributed Hash Table:** Organizes data across multiple SQLite databases for scalability.
* **Pythonic API:**  Offers a simple and intuitive API for interacting with the key-value store. 
* **Lightweight and Easy to Use:**  Minimal dependencies and straightforward setup.
* **Flexible Data Types:**  Supports string keys and various value types, including strings, numbers, booleans, lists, and dictionaries (serialized as JSON).

## Use Cases

* **Caching:** Store frequently accessed data, such as API responses, database query results, or computed values.
* **Session Management:**  Manage user sessions in web applications.
* **Temporary Data Storage:** Store transient data for short-lived tasks or calculations.


## Project
Thanks for checking out the beta release of LiteStash.  More features are in the works.  The Github is a mirror of the project at this time.  LiteStash is under active development and working towards the first release.

Contact mail@mesotron.dev with questions & requests.
