# 🚀 Session Notes: MCP (Model Context Protocol)

---

## 🧠 1. What is MCP? (Simple Explanation)

**MCP (Model Context Protocol)** is a new open protocol that lets AI models (LLMs) connect to external tools, data sources, files, APIs, databases, and systems in a secure, standardized way.

👉 **Think of MCP as "USB for AI."**  
Just like USB lets any device work with any computer,  
MCP lets any LLM work with any tool or data source.

### In very simple words:

**"MCP is a universal language so AI models can talk to tools."**

### Examples of tools:

- File systems
- Databases
- APIs
- Knowledge bases
- Cloud services
- Browsers
- Custom enterprise systems

---

## 🎯 2. Why MCP Was Introduced?

Before MCP, LLMs had three big problems:

### ❌ Problem 1 — Tool integrations were inconsistent

Each AI app required:

- Custom tool implementations
- Custom APIs
- Special adapters for each LLM provider

**MCP solves this with a standard protocol.**

### ❌ Problem 2 — Tools couldn't be reused

If you built a tool for GPT, it wouldn't work for Claude, Llama, etc.

➡️ **MCP tools are reusable across all AI models.**

### ❌ Problem 3 — Limited & fragile integrations

Older integrations (Plugins, Actions, Agents) were:

- Hard to maintain
- Slow to approve
- Often insecure
- Tightly coupled

### ❌ Problem 4 — No standardized way to connect to local or enterprise systems

Companies needed:

- Private database access
- Filesystems
- Knowledge bases
- Internal APIs

**MCP gives a secure sandboxed way to expose company systems to LLMs.**

---

## 🌟 3. Problems MCP Solves

| Problem | How MCP Solves |
|---------|----------------|
| Lack of standard protocol | Introduces unified tool interface |
| LLMs can't access enterprise data | Tools connect models to private data |
| Difficult to build plugins | Simple, file-based JSON protocol |
| Security issues | Sandboxed, permission-based design |
| Duplication of integrations | One MCP tool → works for multiple models |
| Slow plugin approval processes | No approvals needed; self-hosted |

---

## ⚖️ 4. MCP vs REST API

| MCP | REST API |
|-----|----------|
| Protocol between LLM & tools | Protocol between apps/services |
| Very lightweight, streaming capability | Heavy HTTP-based |
| Real-time LLM tool calling | Not designed for tool calling |
| Sandboxed, LLM-driven | General-purpose |
| Supports file systems, prompts, embeddings | Only supports network endpoints |
| Bi-directional communication | Mostly request-response |

### 🔥 Key Difference:

**REST API is for applications. MCP is for AI models connecting to tools.**

REST API cannot support:

- bidirectional streaming
- LLM-native function calling
- low-latency local tools
- tool discovery and capabilities

**MCP is specifically built for AI.**

---

## 🏛️ 5. MCP Architecture (Visual Mental Model)

```
+------------------------+
|       AI Model         |
|   (OpenAI, Anthropic)  |
+-----------+------------+
            |
            | MCP (JSON-RPC over stdio, WebSocket, etc.)
            |
+-----------v------------+
|      MCP Client        |  ← Built into the LLM or IDE
|  (e.g., ChatGPT, Cursor, Claude) 
+-----------+------------+
            |
            |
+-----------v------------+
|      MCP Server        |
| (Your tool / extension) |
| Provides:              |
|   • Tools              |
|   • Resources          |
|   • Prompts            |
|   • Logging            |
+------------------------+
```

### Key Concept:

- **MCP Server** → Provides capabilities (tools/resources)
- **MCP Client** → LLM or agent that uses those tools

---

## 🧩 6. Components of MCP

### 1. MCP Client

**Used by:**

- ChatGPT
- Claude
- Model-driven IDEs
- Agent frameworks

**It:**

- Discovers tools
- Calls tool handlers
- Requests resources
- Uses prompts from server
- Uses secure permissions

### 2. MCP Server (The tool provider)

**It exposes:**

- 🛠 **Tools** (functions)
- 📄 **Resources** (files, DB queries)
- ✍️ **Prompts** (reusable templates)
- 📦 **Models** (future extension)

### 3. Tool Handlers

Functions provided by MCP server.  
E.g., database query, file creation, weather API call.

### 4. Resource Providers

Make files or data browsable.  
E.g., `/documents/*`, `/data/products.json`

### 5. Transport Layer

MCP supports:

- stdio
- WebSockets
- Custom transports

**Message format:** JSON-RPC 2.0

---

## 🔍 7. Internal Working of MCP (Deep Explanation)

### Discovery

Client connects → server returns what it can do:

- tools
- resources
- prompt templates

### Permissions

Client may ask user:

```
Allow this server to read your files? (Yes/No)
```

### Tool invocation

LLM decides to call a tool (like function calling).

**Example:**

```json
{ "method": "weather.get", "params": {"city": "London"} }
```

### Server executes tool

Calls internal Python/Node functions.

### Streaming response

Server streams output back.

### LLM uses the result

Produces final human-readable answer.

---

## 📦 8. When to Use MCP (Use Cases)

### 🏢 Enterprise Integrations

- Query company databases
- Access knowledge bases
- Interact with internal APIs
- CRM/ERP integrations

### 💻 Developer Productivity

- File system operations
- Code refactoring
- Schema generation
- Local debugging

### 🌐 External API Wrappers

- Weather
- Stock prices
- Email services
- Task management (Jira, Notion)

### 🧠 AI Agents

- AI that executes tasks
- Tool-using assistants
- Autonomous research agents

### 🧰 Automation

- Batch file creation
- Document preparation
- Data extraction
- Report generation

---

## 🚀 9. How to Design a Custom MCP Server (Python)

We use the official mcp Python SDK:

```bash
pip install mcp
```

### 📁 Example Directory

```
my_mcp_server/
  ├── server.py
  ├── requirements.txt
  └── config.json
```

### 🧠 server.py (Basic MCP Server)

```python
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server(name="MyCustomMCP")

# 1. Register a simple tool
@server.tool("math.add")
def add_numbers(a: int, b: int):
    return {"result": a + b}

# 2. Provide a resource (file directory)
@server.resource("localfiles", path="./data")
def resource_handler(path: str):
    with open(path, "r") as f:
        return TextContent(f.read())

# 3. Start the MCP server
if __name__ == "__main__":
    server.run()
```

---

## 🧪 10. Real-time Hands-on Project

### 🔥 Project: Build an MCP Server to Manage TODO Tasks

### 📝 Features:

- Add tasks
- List tasks
- Mark tasks as completed
- LLM can manage your entire task list via MCP

### 📁 server.py — TODO Manager MCP

```python
from mcp.server import Server
from mcp.types import ListResult

server = Server(name="TodoMCP")
todos = []

@server.tool("todo.add")
def add_task(task: str):
    todos.append({"task": task, "done": False})
    return {"message": "Task added", "task": task}

@server.tool("todo.list")
def list_tasks():
    return {"tasks": todos}

@server.tool("todo.complete")
def complete_task(index: int):
    if 0 <= index < len(todos):
        todos[index]["done"] = True
        return {"message": "Task completed", "task": todos[index]}
    return {"error": "Invalid task index"}

if __name__ == "__main__":
    server.run()
```

### 🧪 How it works in ChatGPT/Claude (Example Interaction)

**User:**
```
"Add a task to buy groceries."
```

**LLM internally calls:**

```json
{ "method": "todo.add", "params": {"task": "buy groceries"} }
```

**Server responds:**

```json
{ "message": "Task added", "task": "buy groceries" }
```

**LLM Final Answer:**
```
"I added the task buy groceries to your TODO list."
```

---

## 🎉 11. Extended Enhancements You Can Add

- Persistent storage (SQLite)
- Priority tagging
- Deadlines
- Calendar sync
- Notifications

---

## 🎓 End of Session — Summary

| Topic | Explanation |
|-------|-------------|
| What is MCP? | A universal protocol that connects LLMs to tools |
| Why introduced? | Solve fragmentation, improve integration |
| Architecture | Client ↔ MCP Protocol ↔ Server |
| Components | Tools, resources, prompts, transports |
| Use cases | Enterprise, automation, agents, apps |
| Build custom server | Python SDK, tool handlers |
| Hands-on project | TODO Task Manager MCP server |