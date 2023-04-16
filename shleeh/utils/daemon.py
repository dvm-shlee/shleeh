def kill_daemon(daemon_obj):
    if daemon_obj.is_alive():
        if daemon_obj._tstate_lock != None:
            daemon_obj._tstate_lock.release()
    else:
        pass
