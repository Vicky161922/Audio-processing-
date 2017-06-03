import numpy as np
import wave
import struct    
        #some useful variables
window_size=2205
threshold=1000
sampling_freq = 44100	# Sampling frequency of audio signal
def sum_square(i,j,array):
    answer=0
    for x in range(i,j):
            answer=array[x]**2+answer

    return answer
def play(sound_file):
    file_length = sound_file.getnframes()
    sound = np.zeros(file_length)
    for i in range(file_length):
        data = sound_file.readframes(1)
        data = struct.unpack("<h", data)
        sound[i] = int(data[0])
    sound = np.divide(sound, float(2**15))	# Normalize data in range -1 to 1
    notes=[ ]
    playednotes=[ ]
    for x in range(0,file_length-window_size,window_size):
          window_avg = (sum_square(x,x+window_size,sound))
          if window_avg>threshold:
             notes.append(x)
    a = 2
    start = 0
    while True:
        for i in range(start, len(notes) - 1):
            if (notes[i + 1] - notes[i] > window_size):
                a = 1
                break

        if (a == 1):
            
            note1 = sound[(notes[start]):((notes[i])+window_size)]

            note1f = np.fft.fft(note1)
            note1abs=np.abs(note1f)
            temp = np.argsort(note1abs)
            imax = temp[len(temp)-1]
            freq = (imax*sampling_freq)/len(note1f)
            if(freq>8500):
                imax = temp[len(temp)-2]
                freq= (imax*sampling_freq)/len(note1f)
            if(freq>1026 and freq<1066):
                playednotes.append("C6")
            elif(freq>1154 and freq<1194):
                playednotes.append("D6")
            elif(freq>1298 and freq<1338):
                playednotes.append("E6")
            elif(freq>1376 and freq<1416):
                playednotes.append("F6")
            elif(freq>1547 and freq<1587):
                playednotes.append("G6")
            elif(freq>1740 and freq<1780):
                playednotes.append("A6")
            elif(freq>1955 and freq<1995):
                playednotes.append("B6")
            elif(freq>2073 and freq<2113):
                playednotes.append("C7")
            elif(freq>2329 and freq<2369):
                playednotes.append("D7")
            elif(freq>2617 and freq<2657):
                playednotes.append("E7")
            elif(freq>2773 and freq<2813):
                playednotes.append("F7")
            elif(freq>3115 and freq<3155):
                playednotes.append("G7")
            elif(freq>3500 and freq<3540):
                playednotes.append("A7")
            elif(freq>3931 and freq<3971):
                playednotes.append("B7")
            elif(freq>4166 and freq<4206):
                playednotes.append("C8")
            elif(freq>4678 and freq<4718):
                playednotes.append("D8")
            elif(freq>5254 and freq<5294):
                playednotes.append("E8")
            elif(freq>5567 and freq<5607):
                playednotes.append("F8")
            elif(freq>6251 and freq<6291):
                playednotes.append("G8")
            elif(freq>7020 and freq<7060):
                playednotes.append("A8")
            elif(freq>7882 and freq<7992):
                playednotes.append("B8")    
            start = i+1
            
        if(i == len(notes)-2):
         break
    
    return(playednotes)
    #find the silence
  
    ############################## Read Audio File #############################
if __name__ == "__main__":
     #code for checking output for all images
     
        for file_number in range(1,6):
            file_name = "Audio_files/Audio_"+str(file_number)+".wav"
            sound_file = wave.open(file_name)
            Identified_Notes = play(sound_file)
            print ("Notes for Audio_file",file_number," = ", Identified_Notes)
            Identified_Notes=[ ]

        
        
        
