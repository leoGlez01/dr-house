CREATE OR REPLACE PROCEDURE treatments_search()
LANGUAGE plpgsql
AS $$
DECLARE
  rec RECORD;
  v_patient_id INT := 1;
  cur CURSOR FOR 
    SELECT description, start_date 
    FROM treatments 
    WHERE record_id IN (SELECT id FROM medical_records WHERE patient_id = v_patient_id);
BEGIN
  -- Abre el cursor
  OPEN cur;
  
  -- Recorre el cursor
  LOOP
    FETCH cur INTO rec;
    EXIT WHEN NOT FOUND; -- Sale del loop cuando no hay más registros

    -- Muestra la información
    RAISE NOTICE 'Tratamiento: %, Fecha: %', rec.description, rec.start_date;
  END LOOP;
  
  -- Cierra el cursor
  CLOSE cur;
END;
$$;
