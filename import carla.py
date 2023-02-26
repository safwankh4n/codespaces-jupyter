import carla
import random

client=carla.Client('local host', 2000)
world=client.get_world()



spectator=world.get_speactator()

transform=world.get_transform()


location=transform.location
rotation=transform.rotation

spectator.set_transform(carla.transform())

vehicle_blueprint=world.get_blueprints(). find("vehicle")
spawn_points=world.get_map(). get_spawn_points()

for i in range(0,50):
    world.try_spawn(random.choice(vehicle_blueprint), random.choice(spawn_points))

ego_vehicle=world.spawn_actor(random.choice(vehicle_blueprint), random.choice(spawn_points))

camera_location= carla.transform(carla.location(z=1.5))
camera_bp=world.get_blueprint_library(). find('sensor.camera.rgb')

camera_spawn=world.spawn_actor(camera_location, camera_bp, attach_to=ego_vehicle)








