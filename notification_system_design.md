
# Stage 1

## Priority Inbox Design

Priority is calculated using:

* Placement (highest priority)
* Result
* Event (lowest priority)

Weights:

* Placement = 3
* Result = 2
* Event = 1

When two notifications have the same weight, the latest notification gets higher priority.

## Algorithm

1. Fetch notifications from API.
2. Assign priority score.
3. Sort notifications by priority.
4. Return Top 10 notifications.

## Efficient Top 10 Maintenance

Use a Min Heap of size 10.

When new notifications arrive:

* Insert notification into heap.
* If heap size exceeds 10 remove lowest priority notification.

Complexity:

* Insert = O(log 10)
* Delete = O(log 10)
* Space = O(10)

## Logging Middleware

The middleware logs:

* API requests
* Errors
* Notification processing events
* Top 10 generation
