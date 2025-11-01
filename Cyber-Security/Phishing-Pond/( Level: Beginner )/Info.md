# Phishing Pond — Writeup
**Room:** Phishing Pond (TryHackMe)  
**Author:** Idan  
**Level:** Easy

## Short Summary
Completed the Phishing Pond room on TryHackMe (Easy level). The goal was to learn basic phishing techniques and how to inspect suspicious pages in a safe environment. I used simple tools to look at requests and headers, and I changed a request parameter to see a different response from the server.

## What I did (Steps)
- Read the room instructions and goals.
- Used Burp Suite (or browser developer tools) to capture the page request.
- Looked at request/response headers and found a parameter to try.
- Changed that parameter and replayed the request — saw a changed response.
- Optionally checked headers with `curl -I <url>`.

## Tools
- Burp Suite (Community) or Browser DevTools  
- curl (optional)

## Outcome & Conclusion
Learned how to inspect web requests and spot indicators of phishing. Next steps: practice more basic labs and add one screenshot showing the intercepted request or `curl` output.

## Artifacts
- screenshots/ — add 1 clear image (Burp intercept or curl output)
