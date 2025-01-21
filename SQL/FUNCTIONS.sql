-- Función para obtener el total de citas de un doctor
CREATE OR REPLACE FUNCTION total_appointments_per_doctor(doctor_id INT)
RETURNS INT AS
$$
BEGIN
    RETURN (SELECT COUNT(*) FROM appointments WHERE doctor_id = doctor_id);
END;
$$ LANGUAGE plpgsql;

-- Función para obtener el historial médico de un paciente
CREATE OR REPLACE FUNCTION get_patient_medical_history(patient_id INT)
RETURNS TABLE(record_id INT, doctor_name VARCHAR, diagnosis TEXT, record_date TIMESTAMP) AS
$$
BEGIN
    RETURN QUERY
    SELECT 
        mr.id,
        u.full_name,
        mr.diagnosis,
        mr.record_date
    FROM medical_records mr
    JOIN doctors d ON mr.doctor_id = d.id
    JOIN users u ON d.user_id = u.id
    WHERE mr.patient_id = patient_id;
END;
$$ LANGUAGE plpgsql;