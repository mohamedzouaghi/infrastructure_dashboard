# infrastructure_dashboard
A dashboard which tracks all the registered servers with the different cloud providers all along with subscriptions details.

# Description
This dashboard is for DevOps and Infrastructure team who need to track all the servers they maintain all along with details like cloud providers, subscriptions expirations etc...
Project Managers can also use this dashboard to track server costs and add them to their project costs.

# Architecture
Technically speaking, dashboard is built upon Django/MySQL stack and there is no Front End by say. This was made intentionally since the Django Admin panel is more than enough for this kind of use case, so you bother with creating a fron end.

# Upcoming releases
Dashboard can be enriched by some simple monitoring capabilities, like current ping status or last seen activity at the server levels. This could be
very interesting for companies with multiple teams, each having multiple environment (Development, Staging, Testing, Production...)
Additionally, there will be some a module to send alerts whenever a server approach its expiration date. This should help infrastructure team to be aware about subscription renewals.
