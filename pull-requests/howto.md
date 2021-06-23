### how to merge the files

Creates html:

```sh
pandoc --toc -s -w html -o pull-requests.html --metadata title="Pull Requests" PR-*.md 
```

Creates md:

```sh
pandoc --toc -s -w markdown -o pull-requests.md PR-*.md  
```