

(def one (read-line))
(def two (read-line))
(def three (read-line))
(def four (read-line))


(use '[clojure.string :refer [join upper-case]])


(defn -main
  [& args]


  (cond
    (= one "1") (println (* (Integer/parseInt two) (Integer/parseInt three)))
    (= one "2") (do (println (str two "!"))
                    (println (* (Integer/parseInt three) (Integer/parseInt four))))))


(-main)


(defn create-input
  [arg]
  (->> (clojure.string/split arg #" ")
       (map #(Integer/parseInt %))))


(if (even? (apply * (create-input (read-line))))
  (println "Even")
  (println "Odd"))


(def input '("101"))

(def input (clojure.string/split (read-line) #" "));

(let [[v] (clojure.string/split (read-line) #" ")]
  (println (apply str (take-last 2 v))))


(println (apply str (reverse (take 2 (reverse (nth input 0))))))

(apply str '("1" "21"))

(def input (clojure.string/split (read-line) #" "));


(def input (clojure.string/split (read-line) #" "))


(let [value (Integer/parseInt (apply str input))
      s (Math/sqrt value)]
  (if (= (* s s) value)
    (println "Yes")
    (println "No")))


(Math/ceil 11.00000000000000000000000000000001)

(Math/ceil (Math/sqrt 49))
(Integer/parseInt (str "100" "100"))


(defn make-bar
  [n init]
  (reduce (fn [acm _] (str acm "]")) init (take n (range))))


(make-bar 5 "A:")


(mapv (fn [a b] (make-bar a b)) (create-input "5 9") ["A:" "B:"])

(mapv (fn [a b] (println (str b a))) (map #(join "" (repeat % "[")) (create-input "5 9")) ["A:" "B:"])


;; => [nil nil]
;; => ["A:[[[[[" "B:[[[[[[[[["]

(take 2 (map (comp upper-case  str char) (range 97 123))); => ("A" "B")
;; => ("a"
;;     "b"
;;     "c"
;;     "d"
;;     "e"
;;     "f"
;;     "g"
;;     "h"
;;     "i"
;;     "j"
;;     "k"
;;     "l"
;;     "m"
;;     "n"
;;     "o"
;;     "p"
;;     "q"
;;     "r"
;;     "s"
;;     "t"
;;     "u"
;;     "v"
;;     "w"
;;     "x"
;;     "y"
;;     "z")


(join "" (repeat 0 "["))
(map #(println %) [1 2])

(mapv println [1 2])


;; (reduce + (take 4 (range)))

;; こういう使い型があるのか。
;; なるほどそれぞれのcolの同じidxのものが関数に渡されるのね
(map vector ["A" "B"] [1 2]); => (["A" 1] ["B" 2])
(map str ["A" "B"] [1 2]); => ("A1" "B2")


(first (range 10)); => 0
(rest (range 10)) ; => (1 2 3 4 5 6 7 8 9)


(defn create-input
  [arg]
  (->> (clojure.string/split arg #" ")
       (apply (fn [op v] (list op (Integer/parseInt v))))))


;; 文字列の+を演算子の+として扱いたいとき
(eval (list (symbol "+") 1 1))


(defn div
  [a b]
  (if (= b 0)
    "error"
    (quot a b)))


(defn operation
  [n a b]
  (cond
    (= "+" n) (+ a b)
    (= "-" n) (- a b)
    (= "*" n) (* a b)
    (= "/" n) (div a b)
    :else "error"))


(take 2 (range 10))
(drop 2 (range 10)); => (2 3 4 5 6 7 8 9)

(conj [2 3] 1); => [2 3 1]
(cons 1 [2 3]); => (1 2 3)

(defn lo
  [col init cnt]
  (if (= (count col) 0)
    init
    (let [[op value] (first col)
          new-value (operation op init value)]
      (if (= new-value "error")
        (println new-value)
        (do
          (println (str cnt ":" new-value))
          (lo (rest col) new-value (inc cnt)))))))


(def start 35000000000)
(def end   35038000000)


(defn compute-seven-digit
  [n]
  (+ (* n 10) (mod n 7)))


(defn seven?
  [n v]
  (= (compute-seven-digit n)) v)


(defn compute
  [start end value]
  (let [m (quot (+ start end) 2)
        v (compute-seven-digit m)]
    ;;    (println (- v value))
    ;;    (println v)
    (cond
      ;; (> v value) (recur start m value)
      ;; (< v value) (recur m end value)
      (> v value) (compute start m value)
      (< v value) (compute m end value)
      (< (Math/abs (- v value)) 1) m
      :else m)))


;; (dosync)
(dotimes [n 10]
  (time (compute 1 end 350328719591)))


(compute-seven-digit 35032871937)

(time (+ 1 1))


;; => 35035285965
(compute-seven-digit (quot (+ start 35035285965) 2))


;; => 350328719370
;; => 350352859651
(> 350352859651 350328719370)

(< 1 2)


(cond
  (= 1 1) 1)


(import '(java.io File))

(def root-package-name (first *command-line-args*))

(def class-loader (.. Thread currentThread getContextClassLoader))


(defn package-name-to-resource-name
  [package-name]
  (.replace package-name \. \/))


(defn classes-tree
  [package-name file]
  (let [branch? (fn [pn-f] (.isDirectory (second pn-f)))
        children (fn [pn-f]
                   (map (fn [f]
                          [(str (first pn-f) "." (.getName f)) f])
                        (.listFiles (second pn-f))))
        is-class-file? (fn [pn-f] (and (.isFile (second pn-f)) (.endsWith (.getName (second pn-f)) ".class")))
        to-class-name (fn [pn-f] (first pn-f))]
    (map to-class-name (filter is-class-file? (tree-seq branch? children [package-name file])))))


(defn find-classes-with-file
  [target-package-name file]
  (let [file-to-class
        (fn [class-name]
          (.loadClass class-loader (.replaceAll class-name "\\.class$" "")))]
    (map file-to-class
         (classes-tree target-package-name file))))


(defn find-classes-with-jar
  [target-package-name jar-file]
  (let [entry-name-to-class-name
        (fn [name] (.replaceAll (.replace name \/ \.) "\\.class$" ""))
        entry-to-class
        (fn [entry] (.loadClass class-loader (entry-name-to-class-name (.getName entry))))
        is-class?
        (fn [entry] (.endsWith (.getName entry) ".class"))]
    (with-open [f jar-file]
      (map entry-to-class
           (filter is-class?
                   (enumeration-seq (.entries f)))))))


(defn find-classes
  [target-package-name]
  (if-let [url (.getResource class-loader (package-name-to-resource-name target-package-name))]
    (case (.getProtocol url)
      "file" (find-classes-with-file target-package-name (File. (.getFile url)))
      "jar" (find-classes-with-jar target-package-name (.. url openConnection getJarFile))
      '())
    '()))


n


(dorun
  (for [c (find-classes root-package-name)] (do (println (.getName c)))))
