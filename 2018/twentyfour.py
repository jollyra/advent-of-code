from util import *


class Attack:
    def __init__(self, damage, attack_type):
        self.damage = damage
        self.attack_type = attack_type


class Group:
    def __init__(self, name, units, hp, attack, initiative, weaknesses, immunities):
        self.name = name
        self.units = units
        self.hp = hp
        self.attack = attack
        self.initiative = initiative
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.army = ''

    def __str__(self):
        return f'{self.name} contains {self.units} effective power: {self.effective_power()} initiative: {self.initiative}'

    def effective_power(self):
        return self.units * self.attack.damage

    def select_target(self, enemy_groups):
        if not len(enemy_groups):
            raise Exception(f'{self.name}: enemy_group is empty')
        if not any(self.calc_damage(dg) for dg in enemy_groups):
            return None
        return sorted(enemy_groups, key=self._target_selection_sort_key)[0]

    def _target_selection_sort_key(self, defending_group):
        return -self.calc_damage(defending_group), -defending_group.effective_power(), -defending_group.initiative

    def calc_damage(self, defending_group):
        if self.attack.attack_type in defending_group.immunities:
            return 0
        if self.attack.attack_type in defending_group.weaknesses:
            return self.effective_power() * 2
        return self.effective_power()


class Army:
    def __init__(self, name):
        self.name = name
        self.groups = {}

    def __str__(self):
        s = f'{self.name}:\n'
        for key in self.groups:
            group = self.groups[key]
            s += f'{group}\n'
        return s

    def add(self, group):
        self.groups[group.name] = group
        group.army = self.name
        return self


def attack_order_sort_key(group):
    return -group.effective_power(), -group.initiative

def decreasing_initiative_key(target_selection):
    attacking_group = target_selection[0] 
    return -attacking_group.initiative

def get_enemy_groups(group, groups):
    return [g for g in groups if g.army != group.army]

def fight(ag, dg):
    dmg = ag.calc_damage(dg)
    casualties = dmg // dg.hp
    if casualties > dg.units:
        casualties = dg.units
    dg.units = dg.units - casualties
    print(f'{ag.army} {ag.name} attacks {dg.army} {dg.name}, killing {casualties} units')

def main():
    immune_group_1 = Group('Group 1', 17, 5390, Attack(4507, 'fire'), 2, ['radiation', 'bludgeoning'], [])
    immune_group_2 = Group('Group 2', 989, 1274, Attack(25, 'slashing'), 3, ['bludgeoning', 'slashing'], ['fire'])
    immune_system_army = Army('Immune System').add(immune_group_1).add(immune_group_2)
    print(immune_system_army)

    infection_group_1 = Group('Group 1', 801, 4706, Attack(116, 'bludgeoning'), 1, ['radiation'], [])
    infection_group_2 = Group('Group 2', 4485, 2961, Attack(12, 'slashing'), 4, ['fire', 'cold'], ['radiation'])
    infection_army = Army('Infection').add(infection_group_1).add(infection_group_2)
    print(infection_army)

    groups = [immune_group_1, immune_group_2, infection_group_1, infection_group_2]  # Don't mutate this!
    while len(immune_system_army.groups) != 0 and len(infection_army.groups) != 0:
        print('-------------------------------------------------------------------')
        ordered_groups = sorted(groups, key=attack_order_sort_key)
        targeted_groups = []
        target_selections = []
        for attacking_group in ordered_groups:
            enemy_groups = get_enemy_groups(attacking_group, groups)
            remaining_enemy_groups = [g for g in enemy_groups if g not in targeted_groups]

            # print('remaining_enemy_groups:')
            # for g in remaining_enemy_groups:
            #     print(g.army, g.name)

            defending_group = attacking_group.select_target(remaining_enemy_groups)
            if defending_group:
                targeted_groups.append(defending_group)
                ag, dg = (attacking_group, defending_group)
                # print(f'{ag.army} {ag.name} would deal {dg.army} {dg.name} {ag.calc_damage(dg)} damage')
                target_selections.append((attacking_group, defending_group))

        target_selections_ordered = sorted(target_selections, key=decreasing_initiative_key)
        for selection in target_selections_ordered:
            fight(*selection)

        for army in [immune_system_army, infection_army]:
            keys_to_delete = []
            for k, v in army.groups.items():
                if v.units <= 0:
                    keys_to_delete.append(k)

            for k in keys_to_delete:
                del army.groups[k]

    print('\n-------------------------------------------------------------------')
    print('Battle finished!\n')
    print(immune_system_army)
    print(infection_army)

if __name__ == '__main__':
    main()
