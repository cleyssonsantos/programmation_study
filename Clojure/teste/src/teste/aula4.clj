(ns teste.aula4)

(def lista [1 2 3 4 5 6 7 8 9 10])

(doseq [item lista]
  (println item))

(def lista1 [30 20 100 422 542])
(println lista1)

(def nova-lista (map #(+ 3 %) lista1))

(println nova-lista)

(doseq [item nova-lista]
  (println item))

(class lista)
(class nova-lista)
(get lista 4)
(update lista 4 inc) ;Msm fn porem "nativa"
(update lista 4 #(+ 1 %)) ;Update recebendo fn # LAMBDA

(println (range 11))
(println (filter even? (range 11)))

(def rangee [1 2 3 4 5])

(println (reduce + rangee))

(defn minha-soma
  [valor-1 valor-2]
  (println "Somando" valor-1 valor-2)
  (+ valor-1 valor-2))

(println (reduce minha-soma rangee))
(println (reduce minha-soma 0 rangee))
