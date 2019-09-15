# set up logging
export HOST_NAME=$(head -1 /proc/self/cgroup|cut -d/ -f3)
export LOG_PATH=$DAT_PATH/logs/$HOST_NAME
mkdir -p $LOG_PATH

# launch service entrypoint
. $BASE_PATH/entrypoint.sh
