-- Crear vista materializada para ver las citas confirmadas de un paciente
CREATE MATERIALIZED VIEW patient_appointments AS
SELECT 
    a.id AS appointment_id,
    ud.full_name AS doctor_name,
    s.name AS specialty,
    a.appointment_date,
    a.start_time,
    a.end_time,
    a.status
FROM appointments a
JOIN patients p ON a.patient_id = p.id
JOIN users u ON p.user_id = u.id
JOIN doctors d ON a.doctor_id = d.id
JOIN users ud ON d.user_id = ud.id
JOIN specialties s ON d.specialty_id = s.id
WHERE u.username = CURRENT_USER;

-- Crear vista materializada para ver el historial médico de un paciente
CREATE MATERIALIZED VIEW patient_medical_history AS
SELECT 
    mr.id AS record_id,
    ud.full_name AS doctor_name,
    mr.diagnosis,
    mr.record_date
FROM medical_records mr
JOIN patients p ON mr.patient_id = p.id
JOIN doctors d ON mr.doctor_id = d.id
JOIN users ud ON d.user_id = ud.id
WHERE p.user_id = (SELECT id FROM users WHERE username = CURRENT_USER);

-- Crear vista materializada para ver los tratamientos de un paciente
CREATE MATERIALIZED VIEW patient_treatments AS
SELECT 
    t.id AS treatment_id,
    t.description,
    t.start_date,
    t.end_date
FROM treatments t
JOIN medical_records mr ON t.record_id = mr.id
JOIN patients p ON mr.patient_id = p.id
WHERE p.user_id = (SELECT id FROM users WHERE username = CURRENT_USER);


-- Esta historia para refrecar las vistas materializadas
REFRESH MATERIALIZED VIEW patient_appointments;
REFRESH MATERIALIZED VIEW patient_medical_history;
REFRESH MATERIALIZED VIEW patient_treatments;
