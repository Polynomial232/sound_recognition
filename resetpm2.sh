#!/bin/sh
_APP="PM2"
_PID="$(ps aux | grep "$_APP" | grep -v grep | awk '{print $2}')"
echo "Kill Process.."
if [ ${#_PID[@]} -gt 0 ]; then
sudo kill $_PID
else
echo "Application Killed"
fi
echo "Kill Success..."