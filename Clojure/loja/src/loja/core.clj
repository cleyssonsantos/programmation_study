(ns loja.core
  (:gen-class))

; ["daniela" "paula" "carlos" "guilherme"] Vetor
; {"Carlos" 37, "Guilherme" 39} Mapa
; '(1 2 3 4 5) Listar ligadas

(def vetor [1 2 3 4 5])

(def novo-vetor (map rest vetor))
(println (first vetor))

(println (rest vetor))
; O rest não daria pra sacar se acabou a sequência
; O next já daria porque sem nada, ele retorna nulo
; O rest sem nada retorna uma sequência vazia

(def vetor [1 2 3 4 5])

(defn meu-map [funcao sequencia]
  "Recebe uma função e uma sequência, e retorna o primeiro elemento."
  (let [primeiro-elemento (first sequencia)]
    (if (not (nil? primeiro-elemento))
      (do
        (funcao primeiro-elemento)
        (meu-map funcao (rest sequencia))))))

(meu-map println vetor)

(def criando-novo-vetor [1 false "Daniela" 42 12])

(defn meu-mapa [funcao sequencia]
  (let [primeiro-elemento (first sequencia)]
    (if (not (nil? primeiro-elemento))
     (do
       (funcao primeiro-elemento)
       (meu-mapa funcao (rest sequencia)))
      (println "Fim do meu mapa."))))

(meu-mapa println criando-novo-vetor)

