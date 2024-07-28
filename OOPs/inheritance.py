class FuelEngine:
    def startEngine(self):
        print("Engine sarted!")


class ElectricEngine:
    def chargeBattery(self):
        print("Battery charged!")


# inheritance
class HybridEngine(FuelEngine, ElectricEngine):
    def drive(self):
        print("Driving with both fuel and electric power.")


myCar = HybridEngine()

# myCar.startEngine()
# myCar.chargeBattery()
# myCar.drive()


class FrontendDev:
    def __init__(self, name, frontendSkills):
        self.name = name
        self.frontendSkills = frontendSkills

    def developeFrontend(self):
        print(f"Developing the frontend using {" ".join(self.frontendSkills)}")


class BackendDev:
    def __init__(self, name, backendSkills):
        self.name = name
        self.backendSkills = backendSkills

    def developeBackend(self):
        print(f"Developing the backend using {" ".join(self.backendSkills)}")


class FullStackDev(FrontendDev, BackendDev):
    def __init__(self, name, frontendSkills, backendSkills):
        self.name = name
        FrontendDev.__init__(self, name, frontendSkills)
        BackendDev.__init__(self, name, backendSkills)


devAlex = FullStackDev(
    "Alex",
    ["JavaScript", "React.Js", "Tailwind CSS", "Next.Js"],
    ["Node.Js", "Express.Js", "MongoDB", "Django"],
)

print(devAlex.frontendSkills)
print(devAlex.backendSkills)
devAlex.developeFrontend()
devAlex.developeBackend()
