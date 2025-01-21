-- Disparador para actualizar el estado de la cita cuando se confirme
CREATE OR REPLACE FUNCTION update_appointment_status()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.status IS DISTINCT FROM OLD.status THEN
        UPDATE appointments
        SET status = NEW.status
        WHERE id = NEW.id;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Crear el disparador para la tabla de citas
CREATE TRIGGER update_appointment_status_trigger
AFTER UPDATE ON appointments
FOR EACH ROW
WHEN (OLD.status IS DISTINCT FROM NEW.status)
EXECUTE FUNCTION update_appointment_status();