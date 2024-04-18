(ns loja.meumapa)

(def vetor [1 "Aloha" false 29 "Talaz"])

#_(defn meu-map [funcao sequencia]
  (let [primeiro-elemento (first sequencia)]
    #_{:clj-kondo/ignore [:missing-else-branch]}
    (if (not (nil? primeiro-elemento))
      (do
        (funcao primeiro-elemento)
        (meu-map funcao (rest sequencia))))))

#_(meu-map println vetor)

; TAIL RECURSION -> Otimização do CLJ pra não estourar o "laço"
(defn meu-map [funcao sequencia]
  (let [primeiro-elemento (first sequencia)]
    #_{:clj-kondo/ignore [:missing-else-branch]}
    (if (not (nil? primeiro-elemento))
      (do
        (funcao primeiro-elemento)
        (recur funcao (rest sequencia)))))) ; Recur aqui


(def numeros [1 2 3 4 5])

; Variação de POLIMORFISMO em OO.
(defn conta-quantidade-elementos 
  ([sequencia]
   (conta-quantidade-elementos 0 sequencia))
  ([total-ate-agora sequencia]
   (let [sequencia-nao-esta-vazia? (not (empty? sequencia))]
     (if sequencia-nao-esta-vazia?
       (recur (inc total-ate-agora) (rest sequencia))
       (println "A quantidade de elementos do vetor passado é:" total-ate-agora)))))

(conta-quantidade-elementos 0 numeros)

(println (next [])) ; O retorno vazio é nil
(println (rest [])) ; O retorno vazio é ()

(def numeros-novos [1 2 3 4 5 6 7 8 9])

(defn nova-soma [elementos]
  (loop [total-ate-agora 0
         elementos-restantes elementos]
    (if (not (empty? elementos-restantes))
      (recur (inc total-ate-agora) (rest elementos-restantes))
      total-ate-agora)))

(println (nova-soma numeros-novos))