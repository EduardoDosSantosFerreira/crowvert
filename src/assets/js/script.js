    // Adicione este script no final do body ou em um arquivo JS separado
    document.addEventListener('DOMContentLoaded', function () {
        // Efeito de contagem nos números e letras (como %, s)
        const statNumbers = document.querySelectorAll('.stat-number');
  
        statNumbers.forEach(stat => {
          const dataCount = stat.getAttribute('data-count');
          let sufixo = '';
          let numeroAlvo = 0;
  
          if (dataCount) {
            // Expressão regular para separar número e sufixo (letras, %, s, etc)
            const match = dataCount.trim().match(/^([\d.,]+)([a-zA-Z%]+)?$/);
            if (match) {
              numeroAlvo = parseFloat(match[1].replace(',', '.'));
              sufixo = match[2] ? match[2] : '';
            }
          }
  
          const duration = 2000; // 2 segundos
          const steps = 20;
          const increment = numeroAlvo / steps;
          let current = 0;
  
          const timer = setInterval(() => {
            current += increment;
            if (current >= numeroAlvo) {
              clearInterval(timer);
              current = numeroAlvo;
            }
            // Se for inteiro, mostra inteiro, se for decimal, mostra decimal
            if (sufixo === '%' || sufixo === 's') {
              stat.textContent = Math.floor(current) + sufixo;
            } else if (sufixo.length > 0) {
              stat.textContent = Math.floor(current) + sufixo;
            } else {
              stat.textContent = Math.floor(current);
            }
          }, duration / steps);
        });
  
        // Inicialize o particles.js (você precisará incluir a biblioteca particles.js)
        // particlesJS.load('particles-js', 'particles-config.json');
      });