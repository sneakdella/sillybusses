#/usr/bin/bash

echo "Pushing to github."
echo "CTRL+C to cancel, or put in a comment for the push to origin."
read comment

git add .
git commit -m "$comment"

git push origin master
