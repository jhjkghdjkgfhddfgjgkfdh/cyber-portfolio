<<<<<<< HEAD
# Phishing Pond — Writeup
**Room:** Phishing Pond (TryHackMe)  
**Author:** Idan

## Short Summary
Completed the Phishing Pond room on TryHackMe. The goal was to learn phishing techniques and practice analyzing malicious pages and emails in a safe environment. I used Burp Suite to intercept and inspect HTTP requests and responses, examined relevant headers and links, and successfully modified a request parameter to observe a change in the server response. This confirmed the ability to analyze phishing flows and manipulate requests for testing and learning purposes.

## What I did (Steps)
- Started by reading the room objectives and mapping tasks (identify suspicious URL, inspect request/response).
- Intercepted traffic with **Burp Suite** (Proxy → Intercept), captured the target request and forwarded it to **Repeater**.
- Inspected request/response headers and body to locate the parameter to test.
- Modified the parameter in Repeater and replayed the request — observed a different server response that demonstrated the vulnerable/interesting behavior.
- Optionally checked page headers with `curl -I <url>` and performed basic DNS lookup with `nslookup <domain>`.

## Tools
- Burp Suite (Community) — intercept & repeater  
- Browser DevTools — network inspection  
- curl, nslookup — quick header/DNS checks
=======
\# Phishing Pond — Writeup

\*\*Room:\*\* Phishing Pond (TryHackMe)  

\*\*Author:\*\* Idan



\## Short Summary

Completed the Phishing Pond room on TryHackMe. The goal was to learn phishing techniques and practice analyzing malicious pages and emails in a safe environment. I used Burp Suite to intercept and inspect HTTP requests and responses, examined relevant headers and links, and successfully modified a request parameter to observe a change in the server response. This confirmed the ability to analyze phishing flows and manipulate requests for testing and learning purposes.



\## What I did (Steps)

\- Started by reading the room objectives and mapping tasks (identify suspicious URL, inspect request/response).

\- Intercepted traffic with \*\*Burp Suite\*\* (Proxy → Intercept), captured the target request and forwarded it to \*\*Repeater\*\*.

\- Inspected request/response headers and body to locate the parameter to test.

\- Modified the parameter in Repeater and replayed the request — observed a different server response that demonstrated the vulnerable/interesting behavior.

\- Optionally checked page headers with `curl -I <url>` and performed basic DNS lookup with `nslookup <domain>`.



\## Tools

\- Burp Suite (Community) — intercept \& repeater  

\- Browser DevTools — network inspection  

\- curl, nslookup — quick header/DNS checks



\## Outcome \& Conclusion

Successfully demonstrated an ability to analyze a phishing scenario: intercept HTTP traffic, inspect/mutate requests, and verify server behavior. Recommended next steps: practice identifying SPF/DKIM/DMARC issues and recreate the scenario in a local sandbox (MailHog/smtp4dev) for safer testing.
>>>>>>> a646a89 (Add short Phishing Pond writeup)

## Outcome & Conclusion
Successfully demonstrated an ability to analyze a phishing scenario: intercept HTTP traffic, inspect/mutate requests, and verify server behavior. Recommended next steps: practice identifying SPF/DKIM/DMARC issues and recreate the scenario in a local sandbox (MailHog/smtp4dev) for safer testing.
