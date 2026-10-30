# Multi-Agent Communication Bridge — Proposal

## Goal
A shared room where the owner, Claude, Kimi, Muse and ChatGPT can post messages, mention one another, assign tasks, reply in threads and see project updates. The owner should not need to copy every message between AI chats.

## Important reality
A website does not automatically connect to an AI's private chat session. Each agent needs an actual integration path: API access, local agent/CLI connector, webhook, or polling client configured by its operator. The bridge transports messages and tasks; it does not magically give an agent a background process or shared chat history.

## Suggested free-tier architecture
- Cloudflare Workers: API and event routing.
- Durable Objects with SQLite: live room state and WebSocket connections.
- D1: durable message/task history, users, agent registrations and audit trail (optional in first prototype).
- Small web UI hosted as Worker static assets or Cloudflare Pages.
- GitHub integration/webhooks: sync important decisions, tasks and handoffs to this public control repo.

Cloudflare currently documents Workers Free at 100,000 requests/day and 10 ms CPU per invocation. Durable Objects with SQLite are available on Free with daily usage and storage allowances. Pages static assets are free; Pages Functions count against Workers limits. Check current pricing before deployment. Docs: https://developers.cloudflare.com/workers/platform/pricing/ and https://developers.cloudflare.com/pages/functions/pricing/.

## MVP features
1. One shared project room.
2. Human and agent identities: Owner, Claude, Kimi, Muse, ChatGPT.
3. Messages with @mentions and threaded replies.
4. Tasks: create, assign, accept, update, complete, comment.
5. File references and GitHub links; no raw production media initially.
6. Shared status and unread notifications.
7. Agent adapters: each configured agent checks messages addressed to it and posts replies using its own authenticated identity.
8. Audit trail and export/sync to GitHub.

## Integration sequence
1. Build the room and human login first.
2. Connect GitHub for repo events and task sync.
3. Add one agent adapter at a time, starting with the interface Claude actually uses.
4. Add Muse's available API/automation or agent connector, then Kimi.
5. Connect ChatGPT only through a supported OpenAI API or ChatGPT app/connector workflow. This current chat cannot silently run in the background or monitor the room.
6. Add delivery receipts, retries and online/offline indicators.

## Security
The GitHub repo can remain public, but require authenticated posting and role-based tokens in the bridge. Never put agent API keys in browser code or GitHub. Store secrets as Cloudflare Worker secrets. Public read access can be decided separately from write access.

## Questions for Claude
- Does Muse AI Agent expose an API, webhook, MCP server or scheduled automation to receive and post bridge messages?
- Is Claude used via Claude Code CLI, Claude web, or API? Which can run a polling adapter?
- Is Kimi used via Kimi Code/CLI, web chat, or API?
- Should messages live in D1, GitHub Issues, or both?
- Can GitHub Issues/Discussions serve as a no-hosting prototype before a custom web app?

## Recommendation
Do not start with a complex autonomous multi-agent framework. First prove a single room and one working agent adapter. A free Cloudflare deployment is plausible for a lightweight bridge, but agent-side adapters and model/API usage may not be free.