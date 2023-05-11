
status=$(ps ax | grep 'python3.8 -u app.py' | grep -v 'grep')

if [[ $1 == "start" ]]; then
 if [[ $status == "" ]]; then
  source venv/bin/activate
  current_log="logs/log_$(date +%F_%H-%M-%S)"
  echo $current_log > "logs/current_log" &
  python3.8 -u app.py > $current_log &
 else
  echo "Aplikasi Sedang Berjalan! Detail: $status"
 fi
elif [[ $1 == "status" ]]; then
 if [[ $status == "" ]]; then
  echo "Aplikasi tidak sedang berjalan"
 else
  echo "Background Detail Aplikasi: $status"
 fi
elif [[ $1 == "kill" ]]; then
 if [[ $status == "" ]]; then
  echo "Tidak Ada Aplikasi Yang Berjalan"
 else
  x=$(ps ax | grep 'python3.8 -u app.py' | grep -v 'grep' | awk {'print $1'})
  kill -9 $x
  echo "killing PID $x"
 fi
elif [[ $1 == "logs" ]]; then
 current_logs=$(cat "logs/current_log")
 tail -f $current_logs
else
 echo "Parameter list: start, status, kill, logs"
fi
