tratamientos <- c("bspline-x2-256", "bspline-x2-1080",
                       "bspline-x4-256", "bspline-x4-1080",
                       "interpolation-x2-256", "interpolation-x2-1080",
                       "interpolation-x4-256", "interpolation-x4-1080")

imagenes <- paste0(sprintf("%03d", 1:80))

imagenes_por_tratamiento <- 10
repeticiones <- 2


diseño <- data.frame(Tratamiento = character(),
                     Imagen_ID = character(),
                     Repeticion = integer(),
                     stringsAsFactors = FALSE)


for (tr in tratamientos) {
  seleccion <- sample(imagenes, imagenes_por_tratamiento)

  for (img in seleccion) {
    for (r in 1:repeticiones) {
      diseño <- rbind(diseño, data.frame(Tratamiento = tr,
                                         Imagen_ID = img,
                                         Repeticion = r,
                                         stringsAsFactors = FALSE))
    }
  }
}

diseño_aleatorizado <- diseño[sample(nrow(diseño)), ]

write.csv(diseño_aleatorizado, "sample.csv", row.names = FALSE)
