class Command:
	def do_getmultiple(self,remotepath):
		"""
        Command to perform get files command from the remote server.

        Args:
            filepath - path of the file to be deleted from the remote server.
        """
		remote_src_dest = remotepath.split(" ")
		if len(remote_src_dest)!=2:
			print ("Enter remotepath and localpath")
		else:
		    try: 
		      response = self._perform_ftp_command('get',remote_src_dest[0], remote_src_dest[1])
		    except IOError as e:
			  print(e)