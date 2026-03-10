# Django Signals Assessment

This project demonstrates the default behavior of Django signals.

## Questions Answered

### 1. Are Django signals synchronous or asynchronous?

Django signals execute synchronously by default.  
In this project, a delay (`time.sleep(3)`) is added inside the signal.  
When the `/sync-test/` endpoint is called, the request waits for the signal to complete, which proves synchronous execution.

### 2. Do signals run in the same thread as the caller?

The thread ID is printed in both the view and the signal using `threading.get_ident()`.  
The output shows the same thread ID, which proves that signals run in the same thread as the caller.

### 3. Do signals run in the same database transaction?

A transaction is created using `transaction.atomic()`.  
Inside the signal a log record is created.  
An exception is raised to force a rollback.  
After rollback, neither the model record nor the signal log remains in the database, which proves the signal ran inside the same transaction.

## Endpoints
