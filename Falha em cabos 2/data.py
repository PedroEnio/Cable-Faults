import matplotlib.pyplot as plt
import numpy as np


class Fault:

    def configFault(self, circuit, dimension):
        self.circuit = circuit
        self.dimension = dimension
        return(circuit, dimension)
    
    def phaseFault(self, phase_a, phase_b, phase_c):
        self.phase_a = np.array(phase_a)
        self.phase_b = np.array(phase_b)
        self.phase_c = np.array(phase_c)  
        return(phase_a, phase_b, phase_c)
    
    def nFaults(self, n_faults, n_prefaults):
        self.n_faults = n_faults
        self.n_prefaults = n_prefaults
        return(n_faults, n_prefaults)

    def plotFault(self):
        #Configurações do gráfico
        fig, ax1 = plt.subplots(1,1)
        h_A = 15 # Phase A high
        h_B = 10 # Phase B high
        h_C = 5  # Phase C high
        desloc = 0.6
        y1 = [h_A,h_B,h_C]
        squad = ['A','B','C']

        #Linha - Fase A
        phaseA_x = np.arange(0, self.dimension)
        phaseA_y = np.repeat(15, self.dimension)
        #Linha - Fase B
        phaseB_x = np.arange(0, self.dimension)
        phaseB_y = np.repeat(10, self.dimension)
        #Linha - Fase C
        phaseC_x = np.arange(0, self.dimension)
        phaseC_y = np.repeat(5, self.dimension)

        #Definindo o eixo Y como A, B e C
        ax1.set_yticks(y1)
        ax1.set_yticklabels(squad, minor=False)

        ax1.set_xticks([0, self.dimension])

        #Plot

        #Plot Falhas - Fase A
        measures_falhas_A = np.array(np.repeat(15,(self.phase_a).size)) # Inserir falhas na fase A do grafico
        #Plot Falhas - Fase B
        measures_falhas_B = np.array(np.repeat(10,(self.phase_b).size)) # Inserir falhas na fase B do grafico
        #Plot Falhas - Fase C
        measures_falhas_C = np.array(np.repeat(5, (self.phase_c).size)) # Inserir falhas na fase C do grafico

        #plot cabos
        plt.plot(phaseA_x, phaseA_y, phaseB_x, phaseB_y, phaseC_x, phaseC_y, color ='black')
        #plot falha A
        plt.plot(self.phase_a,measures_falhas_A, marker = "x", ms = 10, color = 'black', mec = 'red')
        #plot falha B
        plt.plot(self.phase_b,measures_falhas_B, marker = "x", ms = 10, color = 'black', mec = 'red')
        #plot falha C
        plt.plot(self.phase_c,measures_falhas_C, marker = "x", ms = 10, color = 'black', mec = 'red')
        
        
        for index in range(len(self.phase_a)):
            ax1.text(self.phase_a[index], h_A + desloc, self.phase_a[index], size=9, rotation = 45, zorder = index)

        for index in range(len(self.phase_b)):
            if index == 0:
                ax1.text(self.phase_b[index], h_B + desloc, self.phase_b[index], size=9, rotation = 45, zorder = index)
            else:
                if (abs((self.phase_b[index] - self.phase_b[index-1]))/self.dimension < 0.05):
                    pass
                    #ax1.text(self.phase_b[index], h_B - 1.5, self.phase_b[index], size=9, rotation = 45, zorder = index)
                else:
                    ax1.text(self.phase_b[index], h_B + desloc, self.phase_b[index], size=9, rotation = 45, zorder = index)
                    
        for index in range(len(self.phase_c)):
            ax1.text(self.phase_c[index], h_C + desloc, self.phase_c[index], size=9, rotation = 45, zorder = index)
        
        # Inserir comentario no grafico   
        ax1.annotate("Nº total de falhas:", xy=(0.02, 0.07), xycoords=ax1.transAxes, fontsize = 9)
        ax1.annotate(self.n_faults, xy=(0.27, 0.07), xycoords=ax1.transAxes, fontsize = 9) 
            
        ax1.annotate("Nº de falhas pré-localizadas:", xy=(0.02, 0.02), xycoords=ax1.transAxes, fontsize = 9)
        ax1.annotate(self.n_prefaults, xy=(0.41, 0.02), xycoords=ax1.transAxes, fontsize = 9) 
        
        ax1.annotate(
            "As distância da falha é referente ao valor do ensaio de pre-localização, portanto, a distância"
            , xy=(0.01, -0.18), xycoords=ax1.transAxes, fontsize = 7)
        
        ax1.annotate(
            "real pode ser diferente da apresentada acima"
            , xy=(0.01, -0.22), xycoords=ax1.transAxes, fontsize = 7)
      
        #Y limit
        plt.ylim([0,20])

        # Axis label
        plt.xlabel("Distância (m)")
        plt.ylabel("Fase")

        #Title
        plt.title(self.circuit)

