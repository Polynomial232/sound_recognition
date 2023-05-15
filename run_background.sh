
status=$(ps ax | grep 'python3.8 -u app.py' | grep -v 'grep')

start () { 
 source venv/bin/activate
 current_log="logs/log_$(date +%F_%H-%M-%S)"
 echo $current_log > "logs/current_log" &
 python3.8 -u app.py > $current_log &
}

kill_process () {
 x=$(ps ax | grep 'python3.8 -u app.py' | grep -v 'grep' | awk {'print $1'})
 kill -9 $x
 echo "killing PID $x"
}

if [[ $1 == "start" ]]; then
 if [[ $status == "" ]]; then
  start
 else
  echo "Engine Sedang Berjalan! Detail: $status"
 fi
elif [[ $1 == "status" ]]; then
 if [[ $status == "" ]]; then
  echo "Engine tidak sedang berjalan"
 else
  echo "Background Detail Engine: $status"
 fi
elif [[ $1 == "kill" ]]; then
 if [[ $status == "" ]]; then
  echo "Tidak Ada Engine Yang Berjalan"
 else
  kill_process
 fi
elif [[ $1 == "logs" ]]; then
 current_logs=$(cat "logs/current_log")
 tail -f $current_logs
elif [[ $1 == "restart" ]]; then
 kill_process
 start
 echo "Engine direstart"
else
 echo "Parameter list: start, status, kill, logs"
fi
