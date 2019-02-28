class Command:
	def do_getmultiple(self,remotepath):
		"""
        Command to perform 'get multiple' command from the remote server.

        Args:
            remotepath - both Source and Destination.
        """
		file_path = remotepath.split(" ")
		if len(remote_src_dest)!=2:
			print ("Enter remotepath and localpath")
		else:
		    try: 
		      response = self._perform_ftp_command('get',file_path[0], file_path[1])
		    except IOError as e:
			  print(e)
