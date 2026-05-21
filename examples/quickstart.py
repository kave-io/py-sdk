from kave import SyncClient

with SyncClient("localhost:19090") as kave:
    for org in kave.iter_organizations():
        print(org.slug)
