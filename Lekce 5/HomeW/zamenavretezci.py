def zamen(retezec, pozice, znak):
   """Zameni jeden znak v retezci na zadane pozici."""
   novyretezec = retezec[:pozice] + znak + retezec[pozice+1:]
   return novyretezec
